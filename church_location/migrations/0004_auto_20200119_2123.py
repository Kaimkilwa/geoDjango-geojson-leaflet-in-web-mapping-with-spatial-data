# Generated by Django 3.0.2 on 2020-01-19 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church_location', '0003_auto_20200117_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='churchdetails',
            old_name='location',
            new_name='geom',
        ),
    ]
