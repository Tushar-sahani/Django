# Generated by Django 4.2 on 2023-05-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_address_brand_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='shirt',
        ),
    ]
