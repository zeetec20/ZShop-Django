# Generated by Django 3.1.1 on 2020-09-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='nama',
            field=models.CharField(default='name', max_length=20),
        ),
    ]
