# Generated by Django 3.0.6 on 2020-06-06 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unAuth', '0006_auto_20200606_0732'),
        ('Auth', '0003_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notificationBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unAuth.User'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='userId',
            field=models.CharField(max_length=50),
        ),
    ]
