# Generated by Django 4.2.11 on 2024-05-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoezi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinmodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
