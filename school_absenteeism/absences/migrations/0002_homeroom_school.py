# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeroom',
            name='school',
            field=models.ForeignKey(default=1, to='absences.School'),
            preserve_default=False,
        ),
    ]
