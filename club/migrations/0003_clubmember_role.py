# Generated by Django 4.1.5 on 2023-01-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_news_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubmember',
            name='role',
            field=models.CharField(choices=[('P', 'Palyer'), ('C', 'Coach')], default='P', max_length=10),
        ),
    ]
