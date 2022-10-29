from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer, InstrumentSerializer, StudentSerializer, TeacherSerializer, ReviewSerializer, InquirySerializer
from django.http import HttpResponse
from .models import User, Instrument, Student, Teacher, Review, Inquiry
import json


# Create your views here.
def home(request):
    return HttpResponse('<h1>THIS IS MUSICALY<h1>')
def instruments(request):
    instruments = Instrument.objects.all()
    return render(request, 'instruments_list.html', {'instruments': students})
def users(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': students})
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
    

# def update_average_rating(request, pk):
#     average_rating = User.objects.get(pk=pk)
#     return render(request, 'average_rating.html', {'average_rating':average_rating})


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# class GetRatings(APIView):
#     def get(self, request)
#     serializer = UserSerializer(request.User.id)

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

    # the idea is to override the default review "post" or how do I make a custom function with a post api endpoint
    # def create(self, request):
    #     r = Review(title=serializer.title, content=serializer.content, rating=serializer.rating, author=serializer.author, teacher=serializer.teacher)
    #     print(r)
    #     r.save()

    @action(detail=True, methods=['post'])
    def update_rating_fields(self, request, pk=None):
        print('jere ot os')
        print(json.dumps(request.data))
        serializer_class = ReviewSerializer(data=request.data)
        if serializer_class.is_valid():
            print('im here')
            print(json.dumps(serializer_class.data))
            u = User.objects.get(pk=serializer_class.validated_data.teacher)
            print('double here')
            print(u)
            total_review = (u.number_of_ratings * u.average_rating)
            print(total_review)
            number_of_ratings = u.number_of_ratings + 1 
            print(number_of_ratings)
            u.number_of_ratings = number_of_ratings
            print(u.number_of_ratings)
            u.average_rating =(total_review + serializer_class.validated_data.rating) / u.number_of_ratings
            print(u.average_rating)
            print(u.number_of_ratings)
        
        # x = User(number_of_ratings=number_of_ratings, average_rating=average_rating)
            u.save()
            return Response('success')
        else:
            return Response('error')
        
# class AverageRaingView(viewsets.ModelViewSet):
#     serializer_class = UserSerializer

    
class InquiryView(viewsets.ModelViewSet):
    serializer_class = InquirySerializer
    queryset = Inquiry.objects.all()

