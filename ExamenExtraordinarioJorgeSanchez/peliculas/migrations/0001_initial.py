# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clasificacion', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genero', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clave', models.IntegerField(default=0)),
                ('titulo', models.CharField(max_length=125)),
                ('duracion', models.IntegerField(default=0)),
                ('sinopsis', models.CharField(max_length=300)),
                ('clasificacion', models.ForeignKey(to='peliculas.Clasificacion')),
                ('genero', models.ForeignKey(to='peliculas.Genero')),
            ],
        ),
    ]
