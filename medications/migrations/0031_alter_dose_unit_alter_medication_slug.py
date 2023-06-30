# Generated by Django 4.2.2 on 2023-06-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0030_remove_dose_slug_medication_slug_alter_dose_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dose',
            name='unit',
            field=models.CharField(choices=[('dose', 'dose'), ('ml', 'ml'), ('mg', 'mg'), ('pcs', 'pcs')], default='ml', max_length=10),
        ),
        migrations.AlterField(
            model_name='medication',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
    ]
