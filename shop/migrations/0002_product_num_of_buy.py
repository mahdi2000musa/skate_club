# Generated by Django 4.1.5 on 2023-01-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='num_of_buy',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]