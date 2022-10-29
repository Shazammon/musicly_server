# from contextlib import nullcontext
# from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class Instrument(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password, username, **extra_fields):

        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
        email = self.normalize_email(email),
                username = first_name,
                **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username, **extra_fields):
        # if password is None:
        #     raise TypeError('Superusers must have a password.')
        # if email is None:
        #     raise TypeError('Superusers must have an email.')
        # if username is None:
        #     raise TypeError('Superusers must have an username.')     

        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        user = self.create_user(email, password, username, **extra_fields)
        # user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    name = models.CharField(db_index=True, unique=True, max_length=254, blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=240, unique=True)
    is_teacher = models.BooleanField(default = False)
    image = models.CharField(max_length=300, blank=True, null=True)
    tag_line = models.CharField(max_length=200, blank=True, null=True)
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
    instruments = models.ManyToManyField(Instrument, related_name ='teachers', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

class Student(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.TextField(null=True)
    image = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.username


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.TextField(null=True)
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
    author = models.ForeignKey(User, related_name ='reviewer', on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, related_name ='reviewee', on_delete=models.CASCADE)

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
    inquirer = models.ForeignKey(User, related_name ='inquirer', on_delete=models.CASCADE, blank=True, null=True)
    preferred_teacher = models.ForeignKey(User,related_name ='inquiree', on_delete=models.CASCADE, blank=True, null=True)

    def inquirer_name(self):
        return self.inquirer.name

    def preferred_teacher_name(self):
        return self.preferred_teacher.name

    def __str__(self):
        return self.content
    





    