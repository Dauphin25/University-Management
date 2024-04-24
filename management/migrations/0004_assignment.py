# Generated by Django 3.2.10 on 2024-04-24 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_delete_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('text', models.TextField(verbose_name='text')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('professor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='management.professor', verbose_name='Subject')),
                ('subject', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='management.subject', verbose_name='Subject')),
            ],
            options={
                'verbose_name': 'Assignment',
                'verbose_name_plural': 'Assignments',
                'db_table': 'Assignment',
            },
        ),
    ]
