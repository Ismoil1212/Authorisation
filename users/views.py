from django.utils.safestring import mark_safe
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import login, get_backends
from django.core.cache import cache

from allauth.account.utils import complete_signup
from allauth.account import app_settings
from allauth.account.models import EmailAddress

from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm


class UserRegistrationView(CreateView):
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        user = form.save(self.request)
        user.is_active = False
        user.save(),
        self.object = user

        messages.success(
            self.request,
            f"{user.username}, you should cconfirm your account",
        )

        email_address, created = EmailAddress.objects.get_or_create(
            user=user, email=user.email, verified=False, primary=True
        )
        email_address.send_confirmation(self.request)

        messages.info(self.request, "Check your email for confirmation link")

        return complete_signup(
            self.request,
            user,
            app_settings.EMAIL_VERIFICATION,
            self.get_success_url(),
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - registration"
        return context


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):

        user = form.get_user()

        if user:
            auth.login(self.request, user)

        messages.success(
            self.request,
            f"{user.username}, you have successfully logged into your account",
        )

        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - login"
        return context


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "users/profile.html"
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Your profile was successfully updated")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Profile"
        return context


@login_required
def logout(request):

    auth.logout(request)
    if not request.session.get("account_deleted"):
        messages.success(request, "You have successfully logged out")
    else:
        del request.session["account_deleted"]
    return redirect(reverse("main:index"))


login_required


def delete_account(request):
    if request.method == "POST":
        user = request.user
        request.session["account_deleted"] = True
        user.delete()
        logout(request)
        messages.success(request, "Your account has been successfully deleted")
        return redirect(reverse("main:index"))
    return render(request, "users/delete_account.html")
