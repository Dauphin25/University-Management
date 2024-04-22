from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, Page

from ..models.faculty import Faculty
from ..models.student import Student

def get_students(request):
    students = Student.objects.all()
    paginator = Paginator(students, per_page=2)
    page_num = request.GET.get('page', 1)
    page: Page = paginator.get_page(page_num)
    return render(request, 'management/student_list.html', {'students': page})

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