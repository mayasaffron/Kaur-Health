# Generated by Django 3.1.6 on 2021-03-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210326_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(max_length=254, null=True),
        ),
    ]