# Generated by Django 3.2 on 2022-12-23 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0006_auto_20221223_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
