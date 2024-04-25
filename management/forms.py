from django.forms.models import ModelForm
from management.models.faculty import Faculty
from management.models.student import Student
from management.models.attendance import Attendance

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
        fields = ['student', 'date', 'status']
