# Generated by Django 5.0.4 on 2024-04-21 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_alter_student_current_semester_alter_student_gpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, to='management.subject', verbose_name='Prerequisites'),
        ),
        migrations.CreateModel(
            name='CurrentSemesterSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(verbose_name='Points')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student', verbose_name='Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.subject', verbose_name='Subject')),
            ],
            options={
                'verbose_name': 'Current Semester Subject',
                'verbose_name_plural': 'Current Semester Subjects',
            },
        ),
        migrations.CreateModel(
            name='SubjectHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(default=0, verbose_name='Semester')),
                ('points', models.IntegerField(verbose_name='Points')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student', verbose_name='Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.subject', verbose_name='Subject')),
            ],
            options={
                'verbose_name': 'Subject History',
                'verbose_name_plural': 'Subject Histories',
            },
        ),
        migrations.DeleteModel(
            name='StudentSubject',
        ),
    ]
