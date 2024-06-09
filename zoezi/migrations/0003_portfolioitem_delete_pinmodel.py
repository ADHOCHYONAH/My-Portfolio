# Generated by Django 4.2.11 on 2024-05-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoezi', '0002_alter_pinmodel_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='PORTFOLIOITEM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='pinModel',
        ),
    ]