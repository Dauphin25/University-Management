from django.forms.models import ModelForm
from management.models.student import Student
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'