from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

from management.models.faculty import Faculty
from management.models.professor import Professor
from management.models.student import Student
from management.models.subject import Subject
from management.models.current_subject_list import CurrentSemesterSubject
from management.models.subject_history import SubjectHistory
from management.models.taking_subjects import  StudentSubject
from management.models.assignment import Assignment
from management.models.studentassignment import StudentAssignment
from management.models.attendance import Attendance


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
    list_display = (
        'first_name', 'last_name', 'university_email', 'phone_number', 'faculty', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = (
        'first_name', 'last_name', 'university_email', 'phone_number', 'faculty', 'created_at', 'updated_at')
    list_per_page = 20
    ordering = ('created_at',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'professor', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description', 'created_at', 'updated_at')
    list_per_page = 20
    ordering = ('created_at',)


@admin.register(CurrentSemesterSubject)
class CurrentSemesterSubjectAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'points', 'current_semester', 'credit', 'professor')
    list_filter = ('points',)
    search_fields = ('student', 'subject', 'points')
    list_per_page = 20
    ordering = ('student', 'subject')


@admin.register(SubjectHistory)
class SubjectHistoryAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'semester', 'points')
    list_filter = ('semester', 'points')
    search_fields = ('student', 'subject', 'semester', 'points')
    list_per_page = 20
    ordering = ('student', 'subject')

@admin.register(StudentSubject)
class StudentSubjectAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject','professor')



@admin.register(StudentAssignment)
class StudentAssignmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'assignments','text')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject','date','status')
