# Generated by Django 4.2.2 on 2023-06-12 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0009_alter_capacity_capacity_alter_capacity_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capacity',
            old_name='capacity',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='capacity',
            name='unit',
            field=models.PositiveSmallIntegerField(choices=[(1, 'mg'), (2, 'pills'), (3, 'dose'), (0, 'ml')], default=0),
        ),
    ]
