from django.contrib.auth.models import AbstractUser
from django.db import models

from foodgram.constants import (
    MAX_LENGTH_EMAIL,
    MAX_LENGTH_FIRST_NAME,
    MAX_LENGTH_LAST_NAME,
    MAX_LENGTH_PASSWORD,
    MAX_LENGTH_USERNAME,
)

from .validators import username_validator


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    username = models.CharField(
        ('username'),
        max_length=MAX_LENGTH_USERNAME,
        unique=True,
        validators=(username_validator,),
    )
    email = models.EmailField(
        ('email address'),
        max_length=MAX_LENGTH_EMAIL,
        unique=True
    )
    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        verbose_name='Имя пользователя'
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        verbose_name='Фамилия пользователя'
    )
    avatar = models.ImageField(
        upload_to='users/',
        null=True,
        default=''
    )
    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        verbose_name='Пароль пользователя'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                name='unique_user_following',
                fields=['user', 'following']),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='user_youself'
            )
        ]
