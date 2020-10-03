from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField('user_name',max_length=20)
    age = models.IntegerField('user_age')
    salary = models.FloatField('user_salary',)
    address = models.CharField('user_address',max_length=20)

class Login(models.Model):
    username = models.CharField('username',max_length=20,unique=True)
    password = models.CharField('password', max_length=20, unique=True)
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE,related_name='login')

class Address(models.Model):
    city = models.CharField('user_city',max_length=20)
    state = models.CharField('user_state',max_length=20)
    pincode = models.CharField('user_pincode',max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='address')

