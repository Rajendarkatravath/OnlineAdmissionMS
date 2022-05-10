from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.student_sign_up,name='student-sign-up')
]
