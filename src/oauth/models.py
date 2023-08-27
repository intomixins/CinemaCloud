from django.core.validators import FileExtensionValidator
from django.db import models


class AuthUser(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    joindate = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(
        upload_to='',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])]
    )

    @property
    def is_authenticated(self):
        """всегда возвращает True. Это способ узнать, был ли пользователь аутентифицирован"""
        return True

    def __str__(self):
        return self.email



