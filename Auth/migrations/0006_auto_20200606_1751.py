# Generated by Django 3.0.6 on 2020-06-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0005_auto_20200606_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='noificationType',
            field=models.CharField(max_length=10),
        ),
    ]
