# Generated by Django 4.2.4 on 2023-10-30 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0012_alter_teacher_options'),
        ('student', '0003_alter_student_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(max_length=255)),
                ('valandu_skaicius', models.CharField(max_length=255)),
                ('diena', models.CharField(max_length=255)),
                ('valanda_nuo_iki', models.CharField(max_length=255)),
                ('vygdimo_vieta', models.CharField(max_length=255)),
                ('mokytojas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentToBurelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('burelis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burelis.burelis')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
