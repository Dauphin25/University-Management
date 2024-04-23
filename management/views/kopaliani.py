from django.shortcuts import render
from management.models.professor import *
from management.models.student import *
from management.models.subject_history import *
from management.models.current_subject_list import *
from management.models.faculty import *
from management.models.taking_subjects import *
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

def index(request):
    student = Student.objects.all()
    context = {
        'student': student,
    }
    return render(request, 'management/index.html', context)


class Professor_form(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


def professor(request):
    if request.method == 'POST':
        form = Professor_form(request.POST)
        if form.is_valid():
            form.save()

            return redirect("professor")
        else:
            return HttpResponse("შეცდომა")

    else:
        professor = Professor.objects.all()
        form = Professor_form()
        context = {
            'professor': professor,
            'form': form,
        }
    return render(request, 'management/professor.html', context)


class Sabject_form(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


def sabject(request):
    if request.method == 'POST':
        form = Sabject_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sabject")
        else:
            return HttpResponse("შეცდომა")

    else:
        sabject = Subject.objects.all()
        form = Sabject_form()
        sabject = Subject.objects.all()
        form = Sabject_form()
        context = {
            'sabject': sabject,
            'form': form
        }
    return render(request, 'management/subject.html', context)


class StudentSubject_form(ModelForm):
    class Meta:
        model = StudentSubject
        fields = ('subject',)


def takingsabject(request):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            user_logout(request)
            return redirect('takingsabject')
        userId = request.user.first_name
        count = StudentSubject.objects.filter(student__pk=userId).count()
        if request.method == 'POST':
            if count == 7:
                # raise forms.ValidationError("7 საგანი უკვე არჩეულია")
                context = {
                    'studentSubject': StudentSubject.objects.filter(student__pk=userId),
                    'form': StudentSubject_form(),
                    'count': '7 საგანი უკვე არჩეულია',
                }
                return render(request, 'management/takingsabject.html', context)

            form = StudentSubject_form(data=request.POST)
            if form.is_valid():
                a = form.save(commit=False)
                a.student = Student.objects.get(pk=userId)
                print(a.student.first_name)
                form.save()
                return redirect('takingsabject')
            else:
                return HttpResponse("შეცდომა")

        else:
            studentSubject = StudentSubject.objects.filter(student__pk=userId)
            form = StudentSubject_form()
            count = 'სულ არჩეული საგნების ჯამი : ' + str(count)
            context = {
                'studentSubject': studentSubject,
                'form': form,
                'count': count,
            }
    else:
        return redirect('user_login')
    return render(request, 'management/takingsabject.html', context)


def takingsabjectall(request):
    studentSubject = StudentSubject.objects.all()
    context = {
        'studentSubject': studentSubject,
    }
    return render(request, 'management/takingsabject.html', context)


class UserLoginForm(AuthenticationForm):
    username = fields.CharField()
    password = fields.CharField()
    class Meta:
        model = User


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('takingsabject')
    else:
        form = UserLoginForm()
    context = {
        'form_user_login': form,
    }
    return render(request, 'management/user_login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('user_login')