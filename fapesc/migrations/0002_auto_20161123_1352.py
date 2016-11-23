# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fapesc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comunidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128)),
                ('bairro', models.CharField(max_length=128)),
                ('cidade', models.CharField(max_length=128)),
                ('estado', models.CharField(max_length=128)),
                ('teste', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Comunidade',
                'verbose_name_plural': 'Comunidades',
            },
        ),
        migrations.CreateModel(
            name='historico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField(blank=True)),
                ('objeto1', models.CharField(max_length=128)),
                ('relacao', models.CharField(max_length=128)),
                ('objeto2', models.CharField(max_length=128)),
                ('distancia', models.IntegerField(default=0)),
                ('resultado', models.CharField(max_length=128)),
                ('plano_acao', models.CharField(max_length=128)),
                ('usuario', models.ForeignKey(to='fapesc.usuario')),
            ],
            options={
                'verbose_name': 'Historico',
                'verbose_name_plural': 'Historico',
            },
        ),
        migrations.CreateModel(
            name='imagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataImagem', models.DateField(blank=True)),
                ('latitude', models.CharField(max_length=128)),
                ('longitude', models.CharField(max_length=128)),
                ('comunidade', models.ForeignKey(to='fapesc.comunidade')),
            ],
            options={
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
            },
        ),
        migrations.AlterField(
            model_name='casos',
            name='objeto1',
            field=models.ForeignKey(related_name='objeto1', blank=True, to='fapesc.objeto', null=True),
        ),
        migrations.AlterField(
            model_name='casos',
            name='objeto2',
            field=models.ForeignKey(related_name='objeto2', blank=True, to='fapesc.objeto', null=True),
        ),
        migrations.AlterField(
            model_name='casos',
            name='relacao',
            field=models.ForeignKey(to='fapesc.relacao'),
        ),
    ]
