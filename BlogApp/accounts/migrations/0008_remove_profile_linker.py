# Generated by Django 2.1.4 on 2019-05-28 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190528_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='linker',
        ),
    ]
