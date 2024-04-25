from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from management import choices
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _


class Student(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    email = models.EmailField(verbose_name=_('Email'), blank=True)
    phone_number = models.CharField(max_length=255, verbose_name=_('Phone Number'), default=None)
    born_date = models.DateField(verbose_name=_('Born Date'))
    gpa = models.FloatField(
        verbose_name='GPA',
        validators=[MinValueValidator(0.0), MaxValueValidator(4.0)]
    )
    current_semester = models.IntegerField(verbose_name=_('Current Semester'), choices=choices.SEMESTER_CHOICES, default=0)
    faculty = models.ForeignKey('management.Faculty', on_delete=models.CASCADE, verbose_name=_('Faculty'), default=None)
    is_active = models.BooleanField(default=True)
    #image = models.ImageField(upload_to='mediafiles/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.email:
            username = slugify(self.first_name + '-' + self.last_name)
            email = f"{username}@tbc.edu.ge"
            self.email = email
        super().save(*args, **kwargs)
        user = User.objects.create(username=(self.first_name + self.last_name))
        user.password = make_password('User')
        user.first_name = self.id
        user.save()

    class Meta:
        db_table = 'student'
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



