from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import InstrumentSerializer, StudentSerializer, TeacherSerializer, ReviewSerializer, InquirySerializer
from django.http import HttpResponse
from .models import Instrument, Student, Teacher, Review, Inquiry


# Create your views here.
def home(request):
    return HttpResponse('<h1>THIS IS MUSICALY<h1>')
def instruments(request):
    instruments = Instrument.objects.all()
    return render(request, 'instruments_list.html', {'instruments': students})
def students(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})
def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers_list.html', {'teachers': teachers})
def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews_list.html', {'reviews': reviews})
def inquiries(request):
    inquiries = Inquiry.objects.all()
    return render(request, 'inquiries_list.html', {'inquiries': inquiries})
    
class InstrumentView(viewsets.ModelViewSet):
    serializer_class = InstrumentSerializer
    queryset = Instrument.objects.all()
    
class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    
class TeacherView(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    
class ReviewView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    
class InquiryView(viewsets.ModelViewSet):
    serializer_class = InquirySerializer
    queryset = Inquiry.objects.all()