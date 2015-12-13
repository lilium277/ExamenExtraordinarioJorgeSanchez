# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallesRentas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_entrega', models.DateField(verbose_name=b'Fecha de renta')),
                ('pelicula', models.ForeignKey(to='peliculas.Peliculas')),
            ],
        ),
    ]
