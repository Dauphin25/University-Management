from django.forms import DateInput, DateTimeInput
from django.forms.models import ModelForm
from management.models.faculty import Faculty
from management.models.student import Student
from management.models.attendance import Attendance
from management.models.taking_subjects import StudentSubject
from management.models.professor import Professor
from management.models.subject import Subject
from management.models.assignment import Assignment
from management.models.submitassignment import SubmitAssignment


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'


class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'status']



class Professor_form(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


class Sabject_form(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'



class StudentSubject_form(ModelForm):
    class Meta:
        model = StudentSubject
        fields = ('subject',)



class Assignment_form(ModelForm):
    class Meta:
        model = Assignment
        fields = ('name', 'text','subject',)



class SubmitAssignment_form(ModelForm):
    class Meta:
        model = SubmitAssignment
        fields = ('text',)