# Generated by Django 4.1.3 on 2022-12-05 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_alter_classroom_table_alter_student_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProxy',
            fields=[
            ],
            options={
                'ordering': ['-id'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('administracion.student',),
        ),
        migrations.CreateModel(
            name='TeacherProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('administracion.teacher',),
        ),
    ]
