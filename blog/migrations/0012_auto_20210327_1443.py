# Generated by Django 3.1.6 on 2021-03-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
