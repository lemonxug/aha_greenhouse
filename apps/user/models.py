from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserAccount(AbstractUser):
    address = models.CharField('地址', max_length=30,)
    phone = models.CharField('联系电话', max_length=11,)
    avatar = models.ImageField('头像', upload_to='user/avatar/')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username