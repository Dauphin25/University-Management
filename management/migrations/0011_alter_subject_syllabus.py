# Generated by Django 5.0.4 on 2024-04-20 08:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_studentsubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='syllabus',
            field=models.FileField(blank=True, null=True, upload_to='syllabus/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Syllabus'),
        ),
    ]
