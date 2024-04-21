from django.db import models
from management.models import Subject


class CurrentSemesterSubject(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name='Student')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Subject')
    points = models.IntegerField(verbose_name='Points')

    class Meta:
        verbose_name = 'Current Semester Subject'
        verbose_name_plural = 'Current Semester Subjects'

    def __str__(self):
        return f"{self.student} - {self.subject}"

    @property
    def current_semester(self):
        return self.student.current_semester

    @property
    def credit(self):
        return self.subject.number_of_credits

    @property
    def professor(self):
        return self.subject.professor
