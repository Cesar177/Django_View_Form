# Generated by Django 4.1.3 on 2022-12-05 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_studentproxy_teacherproxy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen_Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_and_date', models.DateTimeField(default=datetime.datetime(2022, 12, 5, 21, 33, 34, 265831))),
                ('course', models.CharField(max_length=30)),
                ('evaluator', models.CharField(max_length=50)),
                ('duration_of_the_exam', models.IntegerField(default=0)),
                ('number_of_questions', models.IntegerField(default=0)),
                ('total_score', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'final_examens',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_and_date', models.DateTimeField(default=datetime.datetime(2022, 12, 5, 21, 33, 34, 265831))),
                ('course', models.CharField(max_length=30)),
                ('evaluator', models.CharField(max_length=50)),
                ('project_topic', models.CharField(max_length=100)),
                ('number_of_groups', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'proyects',
            },
        ),
        migrations.CreateModel(
            name='ProyectoProxy',
            fields=[
            ],
            options={
                'ordering': ['project_topic'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('administracion.proyecto',),
        ),
    ]