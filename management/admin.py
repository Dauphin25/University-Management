from django.contrib import admin

from management.models.faculty import Faculty
from management.models.professor import Professor
from management.models.student import Student
from management.models.subject import Subject
from management.models.taking_subjects import StudentSubject


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'born_date', 'gpa', 'current_semester',
                    'faculty', 'is_active', 'created_at', 'updated_at')
    list_filter = ('born_date', 'gpa', 'current_semester', 'is_active', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'born_date', 'gpa', 'current_semester',
                     'faculty', 'is_active', 'created_at', 'updated_at')
    list_per_page = 20
    ordering = ('created_at',)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('title', 'founded_date', 'description', 'email', 'created_at', 'updated_at')
    list_filter = ('founded_date', 'created_at', 'updated_at')
    search_fields = ('title', 'founded_date', 'description', 'email', 'created_at', 'updated_at')
    list_per_page = 20
    ordering = ('created_at',)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'university_email', 'phone_number', 'faculty', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'university_email', 'phone_number', 'faculty', 'created_at', 'updated_at')
    list_per_page = 20
    ordering = ('created_at',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'professor',  'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description',  'created_at', 'updated_at')
    list_per_page = 20
    ordering = ('created_at',)


@admin.register(StudentSubject)
class StudentSubjectAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('student', 'subject', 'created_at', 'updated_at')
    list_per_page = 20
    ordering = ('created_at',)




