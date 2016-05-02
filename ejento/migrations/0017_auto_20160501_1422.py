# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejento', '0016_auto_20150624_0652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternatif',
            old_name='cruelty_free',
            new_name='nama_agen',
        ),
        migrations.RenameField(
            model_name='alternatif',
            old_name='harga',
            new_name='pp',
        ),
        migrations.RenameField(
            model_name='alternatif',
            old_name='isi',
            new_name='sp',
        ),
        migrations.RenameField(
            model_name='alternatif',
            old_name='nama_product',
            new_name='up',
        ),
        migrations.RemoveField(
            model_name='alternatif',
            name='pao',
        ),
        migrations.RemoveField(
            model_name='alternatif',
            name='time',
        ),
        migrations.RemoveField(
            model_name='komentar',
            name='no_telepon',
        ),
    ]
