# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_operation_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operator',
            field=models.CharField(choices=[('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')], max_length=1),
        ),
    ]