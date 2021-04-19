# Generated by Django 2.0.4 on 2018-04-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangotest', '0018_auto_20180427_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='end',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='start',
        ),
        migrations.AddField(
            model_name='booking',
            name='checkin',
            field=models.DateField(default=None, verbose_name='Checkin'),
        ),
        migrations.AddField(
            model_name='booking',
            name='checkout',
            field=models.DateField(default=None, verbose_name='Checkout'),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='poolFacility',
            field=models.BooleanField(default=False, verbose_name='Pool Facility'),
        ),
    ]
