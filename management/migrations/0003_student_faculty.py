# Generated by Django 5.0.4 on 2024-04-19 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='management.faculty', verbose_name='Faculty'),
        ),
    ]