# Generated by Django 4.2.2 on 2023-06-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0005_alter_capacity_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacity',
            name='unit',
            field=models.PositiveSmallIntegerField(choices=[(2, 'pills'), (1, 'mg'), (3, 'dose'), (0, 'ml')], default=0),
        ),
    ]