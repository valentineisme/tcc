# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='casos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distancia', models.IntegerField(default=0)),
                ('resultado', models.CharField(max_length=128)),
                ('plano_acao', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Caso',
                'verbose_name_plural': 'Casos',
            },
        ),
        migrations.CreateModel(
            name='comunidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128)),
                ('bairro', models.CharField(max_length=128)),
                ('cidade', models.CharField(max_length=128)),
                ('estado', models.CharField(max_length=128)),
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
        migrations.CreateModel(
            name='objeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Objeto',
                'verbose_name_plural': 'Objetos',
            },
        ),
        migrations.CreateModel(
            name='relacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Relacao',
                'verbose_name_plural': 'Relacoes',
            },
        ),
        migrations.CreateModel(
            name='restricao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=128)),
                ('distancia', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Restricao',
                'verbose_name_plural': 'Restricoes',
            },
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=128)),
                ('sobrenome', models.CharField(max_length=128)),
                ('dataNasc', models.DateField(null=True, blank=True)),
                ('rua', models.CharField(max_length=128)),
                ('numero', models.IntegerField(default=0)),
                ('bairro', models.CharField(max_length=128)),
                ('cidade', models.CharField(max_length=128)),
                ('estado', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('senha', models.CharField(max_length=128, null=True)),
                ('formacao', models.CharField(max_length=128)),
                ('user', models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.AddField(
            model_name='historico',
            name='usuario',
            field=models.ForeignKey(to='fapesc.usuario'),
        ),
        migrations.AddField(
            model_name='casos',
            name='objeto1',
            field=models.ForeignKey(related_name='objeto1', blank=True, to='fapesc.objeto', null=True),
        ),
        migrations.AddField(
            model_name='casos',
            name='objeto2',
            field=models.ForeignKey(related_name='objeto2', blank=True, to='fapesc.objeto', null=True),
        ),
        migrations.AddField(
            model_name='casos',
            name='relacao',
            field=models.ForeignKey(to='fapesc.relacao'),
        ),
        migrations.AddField(
            model_name='casos',
            name='restricao',
            field=models.ForeignKey(to='fapesc.restricao'),
        ),
    ]
