# imports
from rest_framework import serializers
from .models import Instrument, Student, Teacher, Review, Inquiry

# serializer classes

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('name')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'username', 'email', 'password')
        model = Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'email', 'password', 'bio', 'average_rating', 'years_experience', 'accepting_students', 'instruments')
        model = Teacher

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'content', 'rating', 'author', 'teacher')
        model = Review

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('student_name', 'instrument', 'content', 'availability', 'phone_number', 'email', 'viewed', 'inquirer', 'preferred_teacher')
        model = Inquiry
