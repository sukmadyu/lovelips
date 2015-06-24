# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovelips', '0004_auto_20150624_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternatif',
            name='kri',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
