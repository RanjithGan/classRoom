from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classRoom/', views.classRoom, name='classRoom'),
    path('updateResult/', views.updateResult, name='updateResult'),
    path('updateStudent/<str:pk>/', views.updateStudent, name='updateStudent'),
    path('enroll/', views.enroll, name='enroll'),
    path('grades/', views.grades, name='grades'),
    path('download/', views.download, name='download'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
