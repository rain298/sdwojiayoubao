# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-15 17:39
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20171018_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companypost', DjangoUeditor.models.UEditorField(default='', verbose_name='\u4f01\u4e1a\u4ecb\u7ecd\t')),
            ],
            options={
                'verbose_name': '\u4f01\u4e1a\u4ecb\u7ecd',
                'verbose_name_plural': '\u4f01\u4e1a\u4ecb\u7ecd',
            },
        ),
    ]
