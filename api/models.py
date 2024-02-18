from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Solution(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.TextField(null=True, blank=True)
    questionID = models.CharField(max_length=10,null=True,blank=True)
    extention = models.TextField(null=True,blank=True,default="py")
    