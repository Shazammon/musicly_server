from contextlib import nullcontext
from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, password, username, **extra_fields):

        if email is None:
            raise TypeError('An email must be provided.')
        if not password:
            raise TypeError('Password must be provided.')

        user = self.model(
        email = self.normalize_email(email),
                username = username,
                **extra_fields)
        # user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, password, username, **extra_fields):
        return self._create_user(email, password, username, **extra_fields)
    # def create_superuser(self, email, username, password, **extra_fields):
    #     if password is None:
    #         raise TypeError('Superusers must have a password.')
    #     if email is None:
    #         raise TypeError('Superusers must have an email.')
    #     if username is None:
    #         raise TypeError('Superusers must have an username.')     

        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        # user = self.create_user(email, username, password=password, **extra_fields)
        # user.save(using=self._db)
        # return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=240, unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str_(self):
        return self.email

class Instrument(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    image = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.username


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)
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
    location = models.CharField(max_length=100, blank=True, null=True)

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
    





    