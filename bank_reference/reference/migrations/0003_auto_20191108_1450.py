# Generated by Django 2.2.7 on 2019-11-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0002_auto_20191105_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='BIC',
            field=models.CharField(max_length=200),
        ),
    ]
