# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upd_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
