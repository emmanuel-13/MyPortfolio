# Generated by Django 3.2 on 2022-12-23 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0005_alter_contact_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={},
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='testing', max_length=50),
        ),
    ]
