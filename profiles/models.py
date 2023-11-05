from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    image = ImageField(upload_to="profiles")
    bio = models.TextField(max_length=500,default="Add Profile Bio Here.")
    
    def __str__(self):
        return self.user.username
    

# Signal
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    """create a new profile object when a django user is created"""
    if created:
        Profile.objects.create(user=instance)
