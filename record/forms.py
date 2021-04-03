from django.forms import ModelForm
from .models import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class EnrollForm(ModelForm):
    class Meta:
        model = Enroll
        fields = '__all__'


class AttendForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

