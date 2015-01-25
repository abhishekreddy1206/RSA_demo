# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=1000, null=True, blank=True)),
                ('updated', models.DateField(null=True, blank=True)),
                ('updatedby', models.CharField(max_length=100, null=True, blank=True)),
                ('father_first_name', models.CharField(max_length=20, null=True, blank=True)),
                ('father_middle_name', models.CharField(max_length=20, null=True, blank=True)),
                ('father_last_name', models.CharField(max_length=20, null=True, blank=True)),
                ('mother_first_name', models.CharField(max_length=20, null=True, blank=True)),
                ('mother_middle_name', models.CharField(max_length=20, null=True, blank=True)),
                ('mother_last_name', models.CharField(max_length=20, null=True, blank=True)),
                ('street_address', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=25, null=True, blank=True)),
                ('state', models.CharField(max_length=20, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=20, null=True, blank=True)),
                ('home_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('mother_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('father_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('other_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('mother_email', models.EmailField(max_length=75, null=True, blank=True)),
                ('father_email', models.EmailField(max_length=75, null=True, blank=True)),
                ('esignature', models.CharField(max_length=50, null=True, blank=True)),
                ('signed_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=1000, null=True, blank=True)),
                ('updated', models.DateField(null=True, blank=True)),
                ('updatedby', models.CharField(max_length=100, null=True, blank=True)),
                ('first_name', models.CharField(max_length=20, null=True, blank=True)),
                ('middle_name', models.CharField(max_length=20, null=True, blank=True)),
                ('last_name', models.CharField(max_length=20, null=True, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(max_length=5, null=True, blank=True)),
                ('grade_applying_for', models.CharField(max_length=10, null=True, blank=True)),
                ('ethnicity', models.CharField(max_length=5, null=True, blank=True)),
                ('race', models.CharField(max_length=20, null=True, blank=True)),
                ('ethnicRace', models.CharField(max_length=20, null=True, blank=True)),
                ('prev_school_name', models.CharField(max_length=20, null=True, blank=True)),
                ('current_grade', models.CharField(max_length=10, null=True, blank=True)),
                ('prev_school_address', models.CharField(max_length=100, null=True, blank=True)),
                ('prev_school_city', models.CharField(max_length=25, null=True, blank=True)),
                ('prev_school_state', models.CharField(max_length=20, null=True, blank=True)),
                ('prev_school_zip', models.CharField(max_length=20, null=True, blank=True)),
                ('prev_school_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('prev_school_email', models.EmailField(max_length=75, null=True, blank=True)),
                ('parent', models.ForeignKey(to='registration.Parent', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
