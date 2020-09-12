# Generated by Django 3.0.5 on 2020-09-12 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('userId', models.BigIntegerField()),
                ('userName', models.CharField(max_length=200)),
                ('userTemperature', models.FloatField()),
                ('measuredDatetime', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
                ('measuredPlace', models.CharField(max_length=200)),
            ],
        ),
    ]
