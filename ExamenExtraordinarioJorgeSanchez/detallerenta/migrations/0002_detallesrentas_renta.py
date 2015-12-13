# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0001_initial'),
        ('detallerenta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallesrentas',
            name='renta',
            field=models.ForeignKey(to='rentas.Rentas'),
        ),
    ]
