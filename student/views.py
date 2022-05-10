from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm,StudentUserForm
from django.contrib.auth.models import Group


# Create your views here.
def student_sign_up(request):
    if request.method=='POST':
        student_form=StudentForm(request.POST,request.FILES)
        user_form=StudentUserForm(request.POST)
        if student_form.is_valid() and user_form.is_valid():
            user=user_form.save()
            student=student_form.save(commit=False)
            student.user=user
            student_group,created=Group.objects.get_or_create(name='STUDENT')
            user.groups.add(student_group)
            return HttpResponseRedirect('/student/signin/')
    else:
        student_form=StudentForm()
        user_form=StudentUserForm()
    return render(request,'student/signup.html',{'studentform':student_form,'userform':user_form})