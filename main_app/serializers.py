# imports
from rest_framework import serializers
from .models import Instrument, Student, Teacher, Review, Inquiry

# serializer classes

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
