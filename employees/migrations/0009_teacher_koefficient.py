# Generated by Django 4.2.4 on 2023-10-11 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('koefficient_calculator', '0001_initial'),
        ('employees', '0008_remove_teacher_koefficient'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='koefficient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='koefficient_calculator.koefficient'),
        ),
    ]
