# Generated by Django 3.1.1 on 2020-09-05 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200905_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='verification_code',
            field=models.CharField(max_length=8),
        ),
    ]
