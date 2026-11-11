from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    """
    Класс для переопределения в модели user поля username.
    Что бы у нас запрашивался email и все корректно работало
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email or not email.strip():
            raise ValueError("Email обязателен")
        email = self.normalize_email(email).lower()
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперпользователь должен иметь is_superuser=True")
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Role(models.TextChoices):
        USER = "user", "Пользователь"
        MANAGER = "manager", "Менеджер"

    objects = UserManager()
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER)

    phone = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["email"]