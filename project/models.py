
from email.policy import default
from django.db import models
import uuid
from users.models import profile

# Create your models here.
class project(models.Model):
      owner=models.ForeignKey(profile,null=True,blank=True,on_delete=models.SET_NULL)
      title = models.CharField(max_length=200)
      description = models.TextField(null=True,blank=True)
      featured_image = models.ImageField(null=True,blank=True,default="default.jpg")
      demo_link = models.CharField(max_length=2000,null=True,blank=True)
      source_link = models.CharField(max_length=2000,null=True,blank=True)
      tag =models.ManyToManyField('Tag',blank=True)
      vote_total=models.IntegerField(default=0,null=True,blank=True)
      vote_ratio=models.IntegerField(default=0,null=True,blank=True)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

      def __str__(self):
          return self.title

class review(models.Model):
     VOTE_TYPE = (
         ('up','Up Vote'),
        ('down','Down Vote'),
                  
     )
     #owner = 
     project = models.ForeignKey(project,on_delete=models.CASCADE)
     body =  models.TextField(null=True,blank=True)
     value =  models.CharField(max_length=200, choices=VOTE_TYPE)
     created = models.DateTimeField(auto_now_add=True)
     id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

     def __str__(self):
          return self.value

class Tag(models.Model):
     name = models.CharField(max_length=200)
     created = models.DateTimeField(auto_now_add=True)
     id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

     def __str__(self):
          return self.name




