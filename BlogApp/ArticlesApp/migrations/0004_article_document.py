# Generated by Django 2.1.4 on 2019-05-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticlesApp', '0003_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='document',
            field=models.FileField(default='default.txt', upload_to='documents/'),
        ),
    ]
