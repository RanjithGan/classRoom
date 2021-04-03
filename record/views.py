from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
import csv
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory

# username : ranjith
# password : ranjith
# Create your views here.

@login_required(login_url='login')
def download(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Student name','Roll number','Marks'])

    for student in Student.objects.all().values_list('name','roll_number','marks'):
        writer.writerow(student)
    
    response['Content-Disposition']= 'attatchment; filename="students.csv"'

    return response


def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def classRoom(request):

    if request.method == 'POST':
        attendance = AttendForm(data=request.POST)
        if attendance.is_valid :
            attendance.save()
            return redirect('classRoom')
    students = Student.objects.all()
    form = AttendForm
    context = {'form':form, 'students':students}
    return render(request, 'classRoom.html',context=context)

@login_required(login_url='login')
def updateResult(request):
    students = Student.objects.all()
    form = StudentForm
    context = {'students':students, 'form':form}
    return render(request, 'updateResult.html',context=context)


@login_required(login_url='login')
def updateStudent(request, pk):
    if request.method== 'POST':
        student = Student.objects.get(id=pk)
        student_form = StudentForm(data=request.POST,instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('updateResult')
        else:
            print('invalid')
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    context = {'form':form , 'student':student }
    return render(request, 'updateStudent.html',context=context)


def enroll(request):
    if request.method == 'POST':
        enroll_form = EnrollForm(data=request.POST)
        if enroll_form.is_valid():
            enroll_form.save()
            return redirect('index')
    form = EnrollForm()
    context = {'form':form}
    return render(request, 'enroll.html',context=context)


def grades(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'grades.html',context=context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, "username or password is incorrect")
        context = {}
        return render(request, 'login.html', context=context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

