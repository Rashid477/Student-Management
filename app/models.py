from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    usertype=models.CharField(max_length=50)

    class Meta:
        db_table="usertable"

class Teacher(models.Model):
    Teach=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=20,blank=False,null=False,verbose_name='TeacherName')
    Age=models.PositiveIntegerField()
    Department=models.CharField(max_length=50,blank=False,null=False)
    Experience=models.TextField(blank=True)
    Phoneno=models.IntegerField(blank=False, null=False, unique=True)
    Email=models.EmailField(max_length=254,unique=True,blank=False)

class  Student(models.Model):
    Stud=models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=False, null=False, verbose_name='StudentName')
    DOB = models.DateField( blank=False, null=False,)
    Email = models.EmailField(max_length=150, blank=False,unique=True)
    Phone = models.BigIntegerField(blank=False, null=False, unique=True)
    
    
