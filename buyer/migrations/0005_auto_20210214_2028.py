# Generated by Django 2.1.7 on 2021-02-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0004_auto_20210214_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(default='processing', max_length=40),
        ),
    ]
