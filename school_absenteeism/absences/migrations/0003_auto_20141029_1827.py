# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('absences', '0002_homeroom_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='phone',
            field=localflavor.us.models.PhoneNumberField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='absencereason',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
