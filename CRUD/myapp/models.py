from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    Email_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    subject_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)