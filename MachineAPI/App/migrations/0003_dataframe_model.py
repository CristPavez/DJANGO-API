# Generated by Django 2.2.13 on 2022-06-26 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_test2'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFrame_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dato', models.CharField(max_length=50)),
                ('Drop_Table', models.CharField(max_length=50)),
                ('n_estimators', models.IntegerField(max_length=50)),
                ('bootstrap', models.BooleanField()),
                ('verbose', models.IntegerField(max_length=50)),
                ('max_features', models.CharField(max_length=50)),
            ],
        ),
    ]
