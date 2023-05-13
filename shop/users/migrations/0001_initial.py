# Generated by Django 4.2 on 2023-04-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=20)),
                ('DOB', models.DateField()),
            ],
        ),
    ]
