# Generated by Django 5.0.4 on 2024-04-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('university_email', models.EmailField(max_length=254, verbose_name='University Email')),
                ('current_semester', models.IntegerField(verbose_name='Current Semester')),
                ('gpa', models.FloatField(verbose_name='GPA')),
                ('born_date', models.DateField(verbose_name='Born Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'db_table': 'student',
            },
        ),
    ]