from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import profile

#@receiver(post_save,sender=profile)
def createprofile(sender,instance,created,**kwargs):
    print('profile signal triggered')
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


post_delete.connect(deleteUser,sender=profile)   