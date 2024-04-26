from django.db import models
from .student import Student
from .subject import Subject


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='student')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='subject')
    date = models.DateField(verbose_name='date')
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'attendance'
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.date}'
