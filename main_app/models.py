from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Teachers(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000)
    average_rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    years_experience = models.IntegerField()
    accepting_students = models.BooleanField(
        default = True
    )

    def __str__(self):
        return self.name

class Reviews(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1500)
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    author = models.ForeignKey(Students,default=None)
    teacher = models.ForeignKey(Teachers,default=None)

    def __str__(self):
        return self.title
    