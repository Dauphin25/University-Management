from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, Page

from management.forms import StudentForm
from management.models.faculty import Faculty
from management.models.student import Student

def get_students(request):
    students = Student.objects.all()
    paginator = Paginator(students, per_page=2)
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