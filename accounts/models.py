

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser):

    date_o_b    = models.DateField(blank=False, null=False)
    bio         = models.TextField(blank=False, null=False)

    REQUIRED_FIELDS = ['email', 'date_o_b', 'bio']

    def __str__(self):

        return f'{self.username} | {self.email}'



class Profile(models.Model):

    user    = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    pic     = models.ImageField(default='default_pic.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'