# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0004_auto_20170607_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conducteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conducteur_nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaire_heure', models.IntegerField(default=12)),
                ('horaire_minute', models.IntegerField(default=59)),
            ],
        ),
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ligne_lettre', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=255)),
                ('train_conducteur', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Conducteur')),
                ('train_horaire', models.ManyToManyField(null=True, to='api.Horaire')),
                ('train_ligne', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Ligne')),
            ],
        ),
    ]
