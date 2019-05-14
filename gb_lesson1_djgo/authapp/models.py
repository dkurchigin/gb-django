from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    def __str__(self):
        return "{} | Is Active:{}".format(self.username, self.is_active)