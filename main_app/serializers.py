# imports
from rest_framework import serializers
from .models import User, Instrument, Student, Teacher, Review, Inquiry
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

# function to hash the password


def validate_password(self, value: str) -> str:
    """
    Hash value passed by user.

    :param value: password of a user
    :return: a hashed version of the password
    """
    return make_password(value)


# serializer classes

# define current user
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'name', 'is_teacher', 'image', 'bio', 'average_rating', 'years_experience', 'accepting_students', 'instruments', 'location')
        # exclude = ('password',)

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id', 'name')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'username', 'email', 'password')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'email', 'password', 'bio', 'average_rating', 'years_experience', 'accepting_students', 'instruments')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'rating', 'author', 'teacher')

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ('id', 'student_name', 'instrument', 'content', 'availability', 'phone_number', 'email', 'viewed', 'inquirer', 'preferred_teacher')
