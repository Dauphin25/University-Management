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
            return HttpResponse("დაემატა")
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
            return HttpResponse("დაემატა")
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


