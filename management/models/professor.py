from django.db import models
from django.template.defaultfilters import slugify


class Professor(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='First Name')
    last_name = models.CharField(max_length=255, verbose_name='Last Name')
    university_email = models.EmailField(verbose_name='University Email', blank=True)
    phone_number = models.CharField(max_length=255, verbose_name='Phone Number')
    faculty = models.ForeignKey('management.Faculty', on_delete=models.CASCADE, verbose_name='Faculty', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.university_email:
            username = slugify(self.first_name + '-' + self.last_name)
            email = f"{username}@tbc.edu.ge"
            self.university_email = email
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'professor'
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
