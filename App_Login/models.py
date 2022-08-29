from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user_profile')
    description = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    full_name = models.CharField(max_length=100,blank=True)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    def __str__(self):
        return str(self.user)


class Follow(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    created_date = models.DateTimeField(auto_now_add=True)