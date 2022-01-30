

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser 
from PIL import Image

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pic.path)

        try:
            this = Profile.objects.get(id=self.id)
            if this.pic != self.pic:
                this.pic.delete()
        except: 
            pass