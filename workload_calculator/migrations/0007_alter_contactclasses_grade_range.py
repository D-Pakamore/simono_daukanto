# Generated by Django 4.2.4 on 2023-11-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workload_calculator', '0006_activitytoworkload_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactclasses',
            name='grade_range',
            field=models.IntegerField(choices=[(1, 'Kontaktinė 1 kl.'), (2, 'Kontaktinė 2 kl.'), (3, 'Kontaktinė 3 kl.'), (4, 'Kontaktinė 4 kl.'), (5, 'Kontaktinė 5 kl.'), (6, 'Kontaktinė 6 kl.'), (7, 'Kontaktinė 7 kl.'), (8, 'Kontaktinė 8 kl.')], max_length=100),
        ),
    ]