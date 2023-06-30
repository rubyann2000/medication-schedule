# Generated by Django 4.2.2 on 2023-06-30 14:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0025_alter_medication_time_1_alter_medication_time_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medication',
            name='dosage_1',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='dosage_2',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='dosage_3',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='time_1',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='time_2',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='time_3',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='unit_1',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='unit_2',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='unit_3',
        ),
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('dosage', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('unit', models.CharField(choices=[('ml', 'ml'), ('mg', 'mg'), ('pcs', 'pcs'), ('dose', 'dose')], default='ml', max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doses', to='medications.medication')),
            ],
            options={
                'ordering': ('time',),
            },
        ),
    ]