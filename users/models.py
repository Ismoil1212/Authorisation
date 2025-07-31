from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(
        upload_to="users_images",
        blank=True,
        null=True,
    )
    email = models.EmailField(unique=True, blank=False, null=False)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username
