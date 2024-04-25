from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class Assignment(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    text = models.TextField(verbose_name=_('text'))
    professor = models.ForeignKey('management.Professor', on_delete=models.CASCADE, verbose_name=_('professor'), default=None)
    subject = models.ForeignKey('management.Subject', on_delete=models.CASCADE, verbose_name=_('Subject'), default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Assignment'
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        return f'{self.name}'
