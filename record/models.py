from django.db import models
from django.db.models.signals import post_save


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    marks = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Enroll(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    course_choises = (
        ('UG','UG'),
        ('PG','PG'),
    )
    course = models.CharField(max_length=100, choices=course_choises)

    def __str__(self):
        return self.name

class Audit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    record = models.CharField(max_length=150)

    def __str__(self):
        return self.record


class Attendance(models.Model):
    student_name = models.CharField(max_length=120)
    OPTNS = (
        ('present','present'),
        ('absent','absent')
    )
    attendance = models.CharField(choices=OPTNS,default='absent',max_length=150)

    def __str__(self):
        return self.student_name
    

def student_created(sender, instance , created, **kwargs):
    
    if created:
        content = instance.name + " is created"
        Audit.objects.create(record=content)
        print('student created')

post_save.connect(student_created, sender = Student)


def student_updated(sender, instance , created, **kwargs):
    
    if created == False:
        content = instance.name + " is updated"
        Audit.objects.create(record=content)
        print('student updated')

post_save.connect(student_updated, sender = Student)


def enroll_created(sender, instance , created, **kwargs):
    
    if created:
        content = instance.name + " is enrolled"
        Audit.objects.create(record=content)
        print('enroll created ')

post_save.connect(enroll_created, sender = Enroll)
