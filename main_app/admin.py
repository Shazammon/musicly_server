from django.contrib import admin
# import all created models from .models
from .models import User, Instrument, Student, Teacher, Review, Inquiry

# Register your models here.

admin.site.register(User)
admin.site.register(Instrument)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Review)
admin.site.register(Inquiry)
