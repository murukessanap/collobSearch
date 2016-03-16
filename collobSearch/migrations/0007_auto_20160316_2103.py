# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-16 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collobSearch', '0006_auto_20160316_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyval',
            name='url',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='urlmap',
            name='areaOfInterest',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='urlmap',
            name='searcher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='collobSearch.Searcher'),
        ),
        migrations.AlterUniqueTogether(
            name='keyval',
            unique_together=set([('urlmap', 'url')]),
        ),
        migrations.AlterUniqueTogether(
            name='urlmap',
            unique_together=set([('searcher', 'areaOfInterest')]),
        ),
    ]
