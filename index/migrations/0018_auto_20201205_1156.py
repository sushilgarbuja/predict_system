# Generated by Django 3.1.4 on 2020-12-05 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0017_auto_20201205_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='discription',
            new_name='description',
        ),
    ]
