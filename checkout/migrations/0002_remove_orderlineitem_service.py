# Generated by Django 3.1.6 on 2021-03-12 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='service',
        ),
    ]
