# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejento', '0012_auto_20150624_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternatif',
            name='kri',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
