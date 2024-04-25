from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from management.models.student import Student
from management.models.assignment import Assignment


class StudentAssignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('Student'),
                                default=None)
    assignments = models.ForeignKey(Assignment, on_delete=models.CASCADE, verbose_name=_('Assignment'))
    text = models.TextField(verbose_name=_('text'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'StudentAssignment'
        verbose_name = 'StudentAssignment'
        verbose_name_plural = 'StudentAssignment'

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name}'
