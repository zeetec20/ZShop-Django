# Generated by Django 3.1.1 on 2020-09-05 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_activication_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='activication_code',
            new_name='verification_code',
        ),
    ]