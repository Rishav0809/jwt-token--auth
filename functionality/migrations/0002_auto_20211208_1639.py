# Generated by Django 2.2.10 on 2021-12-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functionality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
