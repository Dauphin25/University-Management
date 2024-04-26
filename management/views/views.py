from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, Page

from management.forms import StudentForm, FacultyForm, AttendanceForm
from management.models import Subject
from management.models.attendance import Attendance
from management.models.faculty import Faculty
from management.models.student import Student
from django.shortcuts import render
from management.models.taking_subjects import StudentSubject

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
                # Redirect to the same page after saving the student
                return redirect('get_students')
            except Exception as e:
                # If an error occurs during form saving, display the error
                error_message = str(e)
                return render(request, 'management/student_list.html',
                              {'students': page, 'form': form, 'error_message': error_message})
        else:
            # If form is not valid, re-render the page with the form and error messages
            return render(request, 'management/student_list.html', {'students': page, 'form': form})

    # If it's a GET request, render the page with the list of students and an empty form
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
