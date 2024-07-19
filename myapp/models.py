
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):

    # nique related_names for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True, help_text='Specific permissions for this user.')



class UploadedImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name


