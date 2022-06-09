from django.db import models
from rest_framework.authtoken.models import Token
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save



class Level(models.Model):
    level = models.CharField(max_length=150)

    def __str__(self):
        return self.level

class College(models.Model):
    college = models.CharField(max_length=200)

    def __str__(self):
        return self.college

class Department(models.Model):
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True,blank=True)
    dept = models.CharField(max_length=150)


    def __str__(self):
        return self.dept

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    img_profile = models.ImageField(upload_to='profile_img/',null=True,blank=True)
    level = models.ForeignKey(Level,on_delete=models.CASCADE,blank=True,null=True,related_name='profile')
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True,related_name='profile')
    teacher = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    def get_image(self):
        return "http://192.168.0.101:8000" + self.img_profile.url
        # return "http://127.0.0.1:8000" + self.img_profile.url

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwarg):
    if kwarg['created']:
        token,create = Token.objects.get_or_create(user=kwarg['instance'])
        Profile.objects.create(user=kwarg['instance'])


post_save.connect(create_profile, sender=User)