from django.core.paginator import Paginator, Page
from management.forms import *
from management.models.attendance import Attendance
from management.models.professor import *
from management.models.current_subject_list import *
from management.models.faculty import *
from management.models.taking_subjects import *
from management.models.studentassignment import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from management.models.submitassignment import *
from django.shortcuts import get_object_or_404
from datetime import datetime
import random


def index(request):
    student = Student.objects.all()
    professor = Professor.objects.all()
    for item in professor:
        print(item.first_name, item.id)
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'სტუმარი'
    context = {
        'student': student,
        'username': username,
    }
    return render(request, 'management/index.html', context)


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


def takingsabject(request):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            user_logout(request)
            return redirect('takingsabject')
        userId = request.user.first_name
        try:
            count = StudentSubject.objects.filter(student__pk=userId).count()
        except:
            user_logout(request)
            return redirect('user_login')
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

            try:
                student = Student.objects.get(pk=userId)
            except:
                user_logout(request)
                return redirect('index')
            # student = get_object_or_404(Student, pk=userId)

            subjects = student.faculty.subject_set.all()
            form.fields['subject'].queryset = subjects

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
                'assignement': assignement,
                # 'studentSubject': studentSubject,
                # 'form': form,
            }
    else:
        return redirect('user_login')
    return render(request, 'management/studentassignment.html', context)


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
                submitAssignment_submited = SubmitAssignment.objects.get(student_id=userId,
                                                                         assignment_id=assignment_id).text
            except:
                submitAssignment_submited = None
            # print(submitAssignment_submited.text)

            form = SubmitAssignment_form
            context = {
                'assignement': assignement,
                'submitAssignment_submited': submitAssignment_submited,
                'form': form,
            }
    else:
        return redirect('user_login')
    return render(request, 'management/submitAssignment.html', context)


def profAssignment(request, assignment_id):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            user_logout(request)
            return redirect('index')
        userId = request.user.first_name
        submitAssignment_submited = SubmitAssignment.objects.filter(assignment__pk=assignment_id)

        context = {
            # 'assignement':assignement,
            'submitAssignment_submited': submitAssignment_submited,
            # 'form': form,
        }
    else:
        return redirect('user_login')
    return render(request, 'management/profAssignment.html', context)



def get_students(request):
    students = Student.objects.all()
    paginator = Paginator(students, per_page=4)
    page_num = request.GET.get('page', 1)
    page = paginator.get_page(page_num)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('get_students')
            except Exception as e:
                error_message = str(e)
                return render(request, 'management/student_list.html',
                              {'students': page, 'form': form, 'error_message': error_message})
        else:
            return render(request, 'management/student_list.html', {'students': page, 'form': form})

    return render(request, 'management/student_list.html', {'students': page, 'form': StudentForm()})


def get_faculties(request):
    faculties = Faculty.objects.all()
    paginator = Paginator(faculties, per_page=2)
    page_num = request.GET.get('page', 1)
    page: Page = paginator.get_page(page_num)
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_faculties')
    return render(request, 'management/faculty_list.html', {'faculties': faculties, 'form': FacultyForm()})


def get_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    return render(request, 'management/student_index.html', {'students': [student]})


def get_faculty(request, pk):
    faculty = get_object_or_404(Faculty, id=pk)
    return render(request, 'management/faculty_index.html', {'faculties': [faculty]})


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'management/subject_list.html', {'subjects': subjects})


def subject_students(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    student_subjects = StudentSubject.objects.filter(subject_id=subject_id)
    students = [student_subject.student for student_subject in student_subjects]

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.instance.subject = subject
            form.save()
            return redirect('subject_list')
    else:
        form = AttendanceForm()

    return render(request, 'management/subject_students.html', {'subject': subject, 'students': students, 'form': form})
def get_attendance(request):
    attendance = Attendance.objects.all()
    context = {
        'attendances': attendance,
    }
    return render(request, 'management/attendance.html', context)
def adddata(request):
    facultys_data = [
        {
            "title": "Gryffindor House",
            "founded_date": datetime(990, 1, 1),
            "description": "Slytherin values ambition, cunning, leadership, and resourcefulness.",
            "email": "slytherin@hogwarts.edu"
        },
        {
            "title": "Hufflepuff House",
            "founded_date": datetime(990, 1, 1),
            "description": "Slytherin values ambition, cunning, leadership, and resourcefulness.",
            "email": "slytherin@hogwarts.edu"
        },

        {
            "title": "Ravenclaw House",
            "founded_date": datetime(990, 1, 1),
            "description": "Slytherin values ambition, cunning, leadership, and resourcefulness.",
            "email": "slytherin@hogwarts.edu"
        },

        {
            "title": "Slytherin House",
            "founded_date": datetime(990, 1, 1),
            "description": "Slytherin values ambition, cunning, leadership, and resourcefulness.",
            "email": "slytherin@hogwarts.edu"
        },
    ]

    for faculty_data in facultys_data:
        faculty = Faculty(**faculty_data)
        faculty.save()

    all_faculty = Faculty.objects.all()
    faculty_ids = [faculty.id for faculty in all_faculty]



    students_data = [
        {"first_name": "Lucius", "last_name": "Malfoy", "born_date": datetime(1980, 1, 1), "gpa": 3.5,
         "email": "lucius.malfoy@example.com",
         "phone_number": "123456789",
         "current_semester": 5,  # Assuming Lucius is in his 5th semester
         "is_active": True, 'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Tom", "last_name": "Riddle", "born_date": datetime(1979, 5, 2), "gpa": 3.8,
         "email": "lucius.malfoy@example.com",
         "phone_number": "123456789",
         "current_semester": 5,  # Assuming Lucius is in his 5th semester
         "is_active": True,  'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Percy", "last_name": "Weasley", "born_date": datetime(1982, 8, 22), "gpa": 3.2,
         "email": "lucius.malfoy@example.com",
         "phone_number": "123456789",
         "current_semester": 5,  # Assuming Lucius is in his 5th semester
         "is_active": True,  'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Bill", "last_name": "Weasley", "born_date": datetime(1981, 12, 30), "gpa": 3.6,
         "email": "lucius.malfoy@example.com",
         "phone_number": "123456789",
         "current_semester": 5,  # Assuming Lucius is in his 5th semester
         "is_active": True,  'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Charlie", "last_name": "Weasley", "born_date": datetime(1980, 4, 15), "gpa": 3.4,
         "email": "lucius.malfoy@example.com",
         "phone_number": "123456789",
         "current_semester": 5,  # Assuming Lucius is in his 5th semester
         "is_active": True,  'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Fred", "last_name": "Weasley", "born_date": datetime(1983, 2, 18), "gpa": 3.7,
         "email": "lucius.malfoy@example.com",
         "phone_number": "123456789",
         "current_semester": 5,  # Assuming Lucius is in his 5th semester
         "is_active": True,  'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "George", "last_name": "Weasley", "born_date": datetime(1983, 2, 18), "gpa": 3.7,
         "email": "lucius.malfoy@example.com",
         "phone_number": "123456789",
         "current_semester": 5,  # Assuming Lucius is in his 5th semester
         "is_active": True,  'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Aberforth", "last_name": "Dumbledore", "born_date": datetime(1982, 7, 30), "gpa": 3.1,
         "email": "lucius.malfoy@example.com",
         "phone_number": "123456789",
         "current_semester": 5,  # Assuming Lucius is in his 5th semester
         "is_active": True,  'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Albus", "last_name": "Dumbledore", "born_date": datetime(1980, 5, 4), "gpa": 3.9,
         "email": "lucius.malfoy@example.com",
         "phone_number": "123456789",
         "current_semester": 5,  # Assuming Lucius is in his 5th semester
         "is_active": True,  'faculty_id': int(random.choice(faculty_ids))},
    ]

    for student_data in students_data:
        student = Student(**student_data)
        student.save()

    professors_data = [
        {"first_name": "Minerva", "last_name": "McGonagall", "university_email": "", "phone_number": "",
         'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Severus", "last_name": "Snape", "university_email": "", "phone_number": "", 'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Pomona", "last_name": "Sprout", "university_email": "", "phone_number": "", 'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Filius", "last_name": "Flitwick", "university_email": "", "phone_number": "", 'faculty_id': int(random.choice(faculty_ids))},
        {"first_name": "Sybill", "last_name": "Trelawney", "university_email": "", "phone_number": "", 'faculty_id': int(random.choice(faculty_ids))},
    ]
    for professor_data in professors_data:
        Professor.objects.create(**professor_data)


    all_professor = Professor.objects.all()
    professor_ids = [professor.id for professor in all_professor]
    # print(professor_ids)

    subjects_data = [
        {"title": "Ancient Runes", "number_of_credits": 3,
         "description": "Study of ancient magical symbols and their meanings.", 'professor_id': int(random.choice(professor_ids))},
        {"title": "Arithmancy", "number_of_credits": 3, "description": "Study of magical properties of numbers.", 'professor_id': int(random.choice(professor_ids))},
        {"title": "Muggle Studies", "number_of_credits": 3,
         "description": "Study of Muggle (non-magical) culture and society.", 'professor_id': int(random.choice(professor_ids))},
        {"title": "Care of Magical Creatures", "number_of_credits": 4,
         "description": "Study of magical creatures and their care.", 'professor_id': int(random.choice(professor_ids))},
        {"title": "Divination", "number_of_credits": 3,
         "description": "Study of predicting the future through various methods.", 'professor_id': int(random.choice(professor_ids))},
        {"title": "Apparition", "number_of_credits": 2, "description": "Study of magical teleportation.", 'professor_id': int(random.choice(professor_ids))},
    ]

    for subject_data in subjects_data:
        subject = Subject.objects.create(**subject_data)
        print(1)
        subject.save()
        print(2)

    return redirect("index")


def removedata(request):
    Student.objects.all().delete()
    Faculty.objects.all().delete()
    User.objects.all().delete()
    return redirect("index")
