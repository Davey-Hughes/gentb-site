# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-25 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mutations', '0014_auto_20181107_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugRegimen',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('desc', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='drug',
            name='regimen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drugs', to='mutations.DrugRegimen'),
        ),
    ]