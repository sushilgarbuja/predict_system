# Generated by Django 3.1.4 on 2020-12-05 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_auto_20201205_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='Username',
            new_name='username',
        ),
    ]
