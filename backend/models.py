from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    number = models.CharField(max_length=32)
    address = models.CharField(max_length=1024)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Others'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    graduation_year = models.CharField(max_length=32)
    section = models.CharField(max_length=32)
    code = models.CharField(max_length=16)
    MEDIUM_CHOICES = (('E', 'English'), ('B', 'Bangla'))
    medium = models.CharField(max_length=1, choices=MEDIUM_CHOICES)
    SHIFT_CHOICES = (('M', 'Morning'), ('D', 'Day'))
    shift = models.CharField(max_length=1, choices=SHIFT_CHOICES)
    form_teacher = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.user.username} - {self.fname} {self.lname}"
