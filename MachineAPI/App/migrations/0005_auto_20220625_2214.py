# Generated by Django 2.2.13 on 2022-06-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20220625_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataframe_model',
            name='image',
            field=models.ImageField(default=1, upload_to='albums/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataframe_model',
            name='n_estimators',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dataframe_model',
            name='verbose',
            field=models.IntegerField(),
        ),
    ]
