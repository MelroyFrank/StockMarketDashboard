# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('dashboard', '0004_stock_stockdailyfifteen_stockdailyfive_stockdailythirty_stockmonthly_stockweekly'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('refresh_time', models.IntegerField(choices=[(60000, '1 min'), (180000, '3 min'), (600000, '10 min'), (1800000, '30 min')], default=60000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='stockdailythirty',
            options={'verbose_name_plural': 'Stock daily thirties'},
        ),
        migrations.AlterModelOptions(
            name='stockmonthly',
            options={'verbose_name_plural': 'Stock monthly'},
        ),
        migrations.AlterModelOptions(
            name='stockweekly',
            options={'verbose_name_plural': 'Stock weekly'},
        ),
        migrations.AlterField(
            model_name='stockdailyfifteen',
            name='closing',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailyfifteen',
            name='high',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailyfifteen',
            name='low',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailyfifteen',
            name='opening',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailyfifteen',
            name='volume',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailyfive',
            name='closing',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailyfive',
            name='high',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailyfive',
            name='low',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailyfive',
            name='opening',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailyfive',
            name='volume',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailythirty',
            name='closing',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailythirty',
            name='high',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailythirty',
            name='low',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailythirty',
            name='opening',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockdailythirty',
            name='volume',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockmonthly',
            name='closing',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockmonthly',
            name='high',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockmonthly',
            name='low',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockmonthly',
            name='opening',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockmonthly',
            name='volume',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockweekly',
            name='closing',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockweekly',
            name='high',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockweekly',
            name='low',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockweekly',
            name='opening',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
        migrations.AlterField(
            model_name='stockweekly',
            name='volume',
            field=models.DecimalField(decimal_places=8, max_digits=20),
        ),
    ]
