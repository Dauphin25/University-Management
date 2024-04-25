from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class SubmitAssignment(models.Model):
    student = models.ForeignKey('management.Student', on_delete=models.CASCADE, verbose_name=_('student'), default=None)
    text = models.TextField(verbose_name=_('text'))
    assignment = models.ForeignKey('management.Assignment', on_delete=models.CASCADE, verbose_name=_('Subject'), default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'SubmitAssignment'
        verbose_name = 'SubmitAssignment'
        verbose_name_plural = 'SubmitAssignment'

