from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class User_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

class Worker_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    ward = models.CharField(max_length=100,null=True)


class Children(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    c_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100,null=True)
    disease = models.CharField(max_length=100, null=True)
    c_address = models.CharField(max_length=100)
    c_contact = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    worker = models.ForeignKey(Worker_reg,on_delete=models.CASCADE)
    center = models.ForeignKey(User_reg,on_delete=models.CASCADE)

class Event(models.Model):
    ename = models.CharField(max_length=100)
    descri = models.CharField(max_length=100)
    eventdate = models.CharField(max_length=100)
    eventtime = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

class Vaccine(models.Model):
    vname = models.CharField(max_length=100)
    vdescri = models.CharField(max_length=100)
    vqty = models.CharField(max_length=100)
    period = models.CharField(max_length=100,null=True)

class Request(models.Model):
    vacci = models.ForeignKey(Vaccine,on_delete=models.CASCADE)
    center_id = models.ForeignKey(User_reg,on_delete=models.CASCADE)
    rqty = models.CharField(max_length=100)
    rdate = models.CharField(max_length=100)
    rstatus = models.CharField(max_length=100)

class Allocate(models.Model):
    message = models.CharField(max_length=100,null=True)
    vaccine = models.ForeignKey(Vaccine,on_delete=models.CASCADE)
    center = models.ForeignKey(User_reg,on_delete=models.CASCADE)
    children = models.ForeignKey(Children,on_delete=models.CASCADE,null=True)
    alstatus = models.CharField(max_length=100)
    tstatus = models.CharField(max_length=100,null=True)
    aldate = models.CharField(max_length=100)
    altime = models.CharField(max_length=100)




