from django.db import models
from django.utils.translation import gettext_lazy as _


class Faculty(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Faculty Title'))
    founded_date = models.DateField(verbose_name=_('Founded Date'))
    description = models.TextField(verbose_name=_('Description'))
    email = models.EmailField(verbose_name=_('Email'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.email:
            username = self.title.lower().replace(' ', '_')
            email = f"{username}@tbc.edu.ge"  # Change domain as needed
            self.email = email
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'faculty'
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.title
