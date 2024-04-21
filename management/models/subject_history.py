from django.db import models
from management.models.subject import Subject
from management.models.student import Student
from django.utils.translation import gettext_lazy as _


class SubjectHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Student')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Subject')
    semester = models.IntegerField(verbose_name='Semester', default=0)
    points = models.IntegerField(verbose_name='Points')

    class Meta:
        verbose_name = 'Subject History'
        verbose_name_plural = 'Subject Histories'

    def __str__(self):
        return f"{self.student} - {self.subject}"

    @property
    def credit(self):
        return self.subject.number_of_credits

    @property
    def professor(self):
        return self.subject.professor

