# Generated by Django 4.2.4 on 2023-09-08 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('koefficient_calculator', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='qualification',
        ),
        migrations.AlterField(
            model_name='employee',
            name='koefficient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='koefficient_calculator.koefficient'),
        ),
    ]
