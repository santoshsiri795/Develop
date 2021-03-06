from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.forms import CharField

# Create your models here.
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver



class profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name= models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=500,blank=True,null=True)
    username=models.CharField(max_length=500,blank=True,null=True)
    location=models.CharField(max_length=500,blank=True,null=True)

    short_intro=models.CharField(max_length=200,blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default="profiles/user-default.png")
    social_github= models.CharField(max_length=200,blank=True,null=True)
    social_twitter= models.CharField(max_length=200,blank=True,null=True)
    social_linkedin= models.CharField(max_length=200,blank=True,null=True)
    social_youtube= models.CharField(max_length=200,blank=True,null=True)
    social_website= models.CharField(max_length=200,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

    def __str__(self):
        return str(self.username)


class skill(models.Model):
    owner= models.ForeignKey(profile,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

    def __str__(self):
        return str(self.name)

#@receiver(post_save,sender=profile)
'''def createprofile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profiles=profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()
    


post_save.connect(createprofile,sender=User)


post_delete.connect(deleteUser,sender=profile)'''   