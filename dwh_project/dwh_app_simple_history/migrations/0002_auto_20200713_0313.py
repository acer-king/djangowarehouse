# Generated by Django 2.2.10 on 2020-07-12 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwh_app_simple_history', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='person',
            unique_together={('first_name', 'last_name')},
        ),
        migrations.AlterUniqueTogether(
            name='personvehicle',
            unique_together={('vehicle',)},
        ),
    ]