# Generated by Django 4.1.1 on 2023-01-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfevents', '0003_alter_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventenquiry',
            name='phone',
            field=models.CharField(default='###', max_length=15, null=True, verbose_name='Phone number'),
        ),
    ]
