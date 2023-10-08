# Generated by Django 4.2.4 on 2023-10-08 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
        ('workload_calculator', '0002_workload_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactclasses',
            old_name='class_grade',
            new_name='grade_range',
        ),
        migrations.RenameField(
            model_name='contactclasses',
            old_name='student_count',
            new_name='student_count_range',
        ),
        migrations.RenameField(
            model_name='workload',
            old_name='yearly_contact_hours',
            new_name='contact_hours',
        ),
        migrations.RenameField(
            model_name='workload',
            old_name='etato_dalis',
            new_name='etat_fraction',
        ),
        migrations.AddField(
            model_name='activitytoworkload',
            name='yearly_hours',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='activities.yearlyhours'),
            preserve_default=False,
        ),
    ]
