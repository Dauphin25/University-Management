from django.forms import ModelForm
from management.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, Page


def get_students(request):
    students = Student.objects.all()
    paginator = Paginator(students, per_page=4)
    page_num = request.GET.get('page', 1)
    page: Page = paginator.get_page(page_num)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('management:get_students')
    return render(request, 'management/student_list.html', {'students': page, 'form': StudentForm()})


def get_faculties(request):
    faculties = Faculty.objects.all()
    paginator = Paginator(faculties, per_page=2)
    page_num = request.GET.get('page', 1)
    page: Page = paginator.get_page(page_num)
    return render(request, 'management/faculty_list.html', {'faculties': page})


def get_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    return render(request, 'management/student_index.html', {'students': [student]})


def get_faculty(request, pk):
    faculty = get_object_or_404(Faculty, id=pk)
    return render(request, 'management/faculty_index.html', {'faculties': [faculty]})



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


class StudentSubject_form(ModelForm):
    class Meta:
        model = StudentSubject
        fields = '__all__'


def takingsabject(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = StudentSubject_form(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("დაემატა")
            else:
                return HttpResponse("შეცდომა")

        else:
            studentSubject = StudentSubject.objects.all()
            form = StudentSubject_form()
            context = {
                'studentSubject': studentSubject,
                'form': form
            }
    else:
        return redirect('user_login')
    return render(request, 'management/takingsabject.html', context)


class UserLoginForm(AuthenticationForm):
    username = fields.CharField()
    password = fields.CharField()
    class Meta:
        model = User
        # fields = ('username', 'email','password1','password2', 'first_name')
    # pass


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # messages.success(request,"თქვენ წარმატებით დარეგისტრირდით")
            return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'form_user_login': form,
    }
    return render(request, 'management/user_login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('user_login')



def addAssignment(request):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            user_logout(request)
            return redirect('addAssignment')
        userId = request.user.last_name
        # count = StudentSubject.objects.filter(student__pk=userId).count()
        if request.method == 'POST':
            form = Assignment_form(data=request.POST)
            if form.is_valid():
                a = form.save(commit=False)
                a.professor = Professor.objects.get(pk=userId)
                print(a.professor.first_name)
                form.save()
                return redirect('addAssignment')
            else:
                return HttpResponse("შეცდომა")

        else:
            try:
                professorSubject = Assignment.objects.filter(professor__pk=userId)
                form = Assignment_form()
                professor = Professor.objects.get(pk=userId)
            except:
                user_logout(request)
                return redirect('user_login')

            subjects = professor.subject_set.all()
            form.fields['subject'].queryset = subjects
            context = {
                'form': form,
                'professorSubject': professorSubject,
            }
    else:
        return redirect('user_login')
    return render(request, 'management/assignment.html', context=context)





def studentassignment(request):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            user_logout(request)
            return redirect('index')
        userId = request.user.first_name
        if request.method == 'POST':
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
            try:
                studentSubjects = StudentSubject.objects.filter(student__pk=userId)
            except:
                user_logout(request)
                return redirect('user_login')
            assignement = Assignment.objects.filter(subject__in=studentSubjects.values_list('subject', flat=True))
            context = {
                'assignement':assignement,
                # 'studentSubject': studentSubject,
                # 'form': form,
            }
    else:
        return redirect('user_login')
    return render(request, 'management/studentassignment.html', context)


class SubmitAssignment_form(ModelForm):
    class Meta:
        model = SubmitAssignment
        fields = ('text',)


def submitAssignment(request, assignment_id):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            user_logout(request)
            return redirect('index')
        userId = request.user.first_name
        if request.method == 'POST':
            form = SubmitAssignment_form(data=request.POST)
            if form.is_valid():
                a = form.save(commit=False)
                a.student = Student.objects.get(pk=userId)
                a.assignment = Assignment.objects.get(pk=assignment_id)
                form.save()
                return redirect('studentassignment')
            else:
                return HttpResponse("შეცდომა")

        else:
            assignement = Assignment.objects.get(pk=assignment_id)
            # subjects = student.faculty.subject_set.all()

            try:
                submitAssignment_submited = SubmitAssignment.objects.get(student_id=userId, assignment_id=assignment_id).text
            except:
                submitAssignment_submited = None
            # print(submitAssignment_submited.text)

            form = SubmitAssignment_form
            context = {
                'assignement':assignement,
                'submitAssignment_submited':submitAssignment_submited,
                'form': form,
            }
    else:
        return redirect('user_login')
    return render(request, 'management/submitAssignment.html', context)




