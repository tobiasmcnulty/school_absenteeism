# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AbsenceReason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomeRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('grade', models.IntegerField(max_length=20, choices=[(0, b'K'), (1, b'1st'), (2, b'2nd'), (3, b'3rd'), (4, b'4th'), (5, b'5th'), (6, b'6th'), (7, b'7th'), (8, b'8th'), (9, b'9th'), (10, b'10th'), (11, b'11th'), (12, b'12th')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_initial', models.CharField(max_length=1)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_initial', models.CharField(max_length=1)),
                ('last_name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(to='absences.Parent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='absence',
            name='home_room',
            field=models.ForeignKey(to='absences.HomeRoom'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='absence',
            name='reason',
            field=models.ForeignKey(to='absences.AbsenceReason'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='absence',
            name='student',
            field=models.ForeignKey(to='absences.Student'),
            preserve_default=True,
        ),
    ]
