# Generated by Django 2.0.6 on 2018-07-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20180711_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Filipino', 'Filipino'), ('German', 'German')], max_length=100, unique=True),
        ),
    ]