from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defaultImg.png',
                              upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
