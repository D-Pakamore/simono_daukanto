# Generated by Django 4.2.4 on 2023-10-30 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_studentclasstoteacher_student_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
    ]