from django.forms.models import ModelForm
from management.models.faculty import Faculty
from management.models.student import Student
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'