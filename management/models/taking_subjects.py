from django.db import models
from management.models.student import Student
from django.utils.translation import gettext_lazy as _


class StudentSubject(models.Model):
    student = models.ForeignKey('management.Student', on_delete=models.CASCADE, verbose_name=_('Student'), default=None)
    subject = models.ForeignKey('management.Subject', on_delete=models.CASCADE, verbose_name=_('Subject'), default=None) # ForeignKey to the semester field of the Student model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student_subject'
        verbose_name = 'Student Subject'
        verbose_name_plural = 'Student Subjects'

    def __str__(self):
        return f'{self.student} - {self.subject}'
