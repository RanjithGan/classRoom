from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Enroll)
admin.site.register(Audit)
admin.site.register(Student)
admin.site.register(Attendance)

