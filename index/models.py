from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Branches(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    data_crate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BranchInfo(models.Model):
    name = models.CharField(max_length=256)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    data_crate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Instructors(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField(blank=True)
    experience = models.IntegerField(blank=True)
    character = models.TextField(blank=True)
    photo = models.ImageField(upload_to='media')
    gender_ch = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(max_length=16, choices=gender_ch)
    branches = models.ForeignKey(Branches, on_delete=models.CASCADE)
    price = models.FloatField(blank=True)
    data_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    user_name = models.CharField(max_length=256)
    subscription = models.IntegerField(blank=True)
    phone_num = models.CharField(max_length=256)
    data = models.DateTimeField(auto_now_add=True)
    sub_inst = models.ForeignKey(Instructors, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    user_topic = models.ForeignKey(Instructors, on_delete=models.CASCADE, blank=True, null=True)
    user_comment = models.TextField(blank=False, null=False)
    user_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


