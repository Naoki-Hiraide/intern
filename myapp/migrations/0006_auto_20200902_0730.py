# Generated by Django 3.1 on 2020-09-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_talk_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
