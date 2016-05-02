# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('no_telepon', models.CharField(max_length=12)),
                ('pesan', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
