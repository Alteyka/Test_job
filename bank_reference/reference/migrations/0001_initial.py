# Generated by Django 2.2.7 on 2019-11-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BIC', models.IntegerField(max_length=9)),
                ('name', models.CharField(max_length=200)),
                ('master_account', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
    ]
