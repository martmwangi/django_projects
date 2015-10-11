# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID',
                 primary_key=True, auto_created=True)),
                ('full_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('interests', models.TextField()),
                ('registered_date', models.DateField(auto_now_add=True)),
                ('last_update', models.DateField(auto_now=True)),
            ],
        ),
    ]
