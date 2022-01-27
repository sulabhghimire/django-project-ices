from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Profile

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, *args, **kwargs):

    if created:
        profile = Profile(user=instance)
        profile.save()
