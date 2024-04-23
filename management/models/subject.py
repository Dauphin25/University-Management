from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from management.models.faculty import Faculty


class Subject(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    faculty = models.ManyToManyField(Faculty, verbose_name=_('Faculty'))
    number_of_credits = models.IntegerField(verbose_name=_('Number of Credits'), default=0)
    description = models.TextField(verbose_name=_('Description'))
    professor = models.ForeignKey('management.Professor', on_delete=models.CASCADE, verbose_name=_('Professor'), default=None)
    syllabus = models.FileField(upload_to='syllabus/', verbose_name=_('Syllabus'), blank=True, null=True,
                                validators=[FileExtensionValidator(['pdf'])])
    # prerequisites = models.ManyToManyField('self', blank=True, verbose_name='Prerequisites')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subject'
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

    def __str__(self):
        return self.title
