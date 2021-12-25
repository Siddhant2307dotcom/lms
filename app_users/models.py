from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse
#import os
def path_and_rename(Instance,filename):
    upload_to='Images/'
    ext=filename.split('.')[-1]
    #get filename
    if instance.user.username:
        filename='User_Profile_Pictures/{}.{}'.format(instance.user.username,ext)
    return os.path.join(upload_to,filename)
# Create your models here.

#Creating a custom userModel
class user_profile(models.Model):
    #Creating one to one of user relationship with in-build model from djangoproject
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=150,blank=True)
    profile_pic=models.ImageField(upload_to=path_and_rename,verbose_name="Profile Picture",blank=True)

    teacher='teacher'
    student='student'
    parent='parent'
    user_types=[
    (teacher,'teacher'),
    (student,'student'),
    (parent,'parent'),
    ]
    user_type=models.CharField(max_length=10,choices=user_types,default=student)

    #Defining a string method that will show the name that will be present on the object of this model
    def __str__(self):
        return self.user.username
        
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
