# Generated by Django 3.0.5 on 2020-09-13 11:22

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
                ('measuredDatetime', models.DateTimeField(primary_key=True, serialize=False)),
                ('measuredPlace', models.CharField(max_length=200)),
            ],
        ),
    ]
