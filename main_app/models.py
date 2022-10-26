from contextlib import nullcontext
from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Instrument(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    average_rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], blank=True, null=True
    )
    years_experience = models.IntegerField(blank=True, null=True)
    accepting_students = models.BooleanField(
        default = True
    )
    instruments = models.ManyToManyField(Instrument, blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=1500)
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    author = models.ForeignKey(Student,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Inquiry(models.Model):
    student_name = models.CharField(max_length=50, blank=True, null=True)
    instrument = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=1500, blank=True, null=True)
    availability = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    viewed = models.BooleanField(default=False)
    inquirer = models.ForeignKey(Student,on_delete=models.CASCADE, blank=True, null=True)
    preferred_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.conent
    





    