# Generated by Django 3.0.7 on 2020-10-13 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0007_auto_20201013_0000'),
    ]

    atomic = False

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='student',
        ),
    ]
