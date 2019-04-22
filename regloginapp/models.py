from django.db import models
class RegistrationData(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    number =models.BigIntegerField()
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=20,blank=True,null=True)
class loginData(models.Model):
    user=models.CharField(max_length=20)
    password1=models.CharField(max_length=20)
