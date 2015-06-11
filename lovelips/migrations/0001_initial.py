# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternatif',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kri', models.TextField(null=True, blank=True)),
                ('harga', models.TextField(null=True, blank=True)),
                ('isi', models.TextField(null=True, blank=True)),
                ('pao', models.TextField(null=True, blank=True)),
                ('time', models.TextField(null=True, blank=True)),
                ('cruelty_free', models.TextField(null=True, blank=True)),
                ('nama_product', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
