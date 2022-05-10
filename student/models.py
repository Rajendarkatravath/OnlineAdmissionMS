from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    contact=models.IntegerField()
    address=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='profile_pic/student/',null=False,blank=False)

