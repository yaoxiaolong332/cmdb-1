# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialnum', models.CharField(max_length=200, unique=True)),
                ('rack_number', models.IntegerField(blank=True, help_text='机柜号', null=True)),
                ('rack_position', models.IntegerField(blank=True, help_text='机柜U位', null=True)),
                ('state', models.IntegerField(choices=[(0, 'Disable'), (1, 'Enable')], db_index=True, default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssetGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agname', models.CharField(db_index=True, max_length=100, unique=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=100)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('machine_type', models.CharField(max_length=200)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cmdb_api.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=200, unique=True)),
                ('lan_ip', models.GenericIPAddressField(db_index=True, protocol='IPv4', unique=True)),
                ('wan_ip', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('vendor', models.CharField(blank=True, max_length=150, null=True)),
                ('cpu', models.CharField(max_length=100)),
                ('disk', models.CharField(max_length=10)),
                ('memory', models.CharField(max_length=20)),
                ('os', models.CharField(max_length=20)),
                ('phost_ip', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cmdb_api.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=20, unique=True)),
                ('realname', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(db_index=True, max_length=100, unique=True)),
                ('assetgroup', models.ManyToManyField(to='cmdb_api.AssetGroup')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='usergroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb_api.UserGroup'),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb_api.AssetType'),
        ),
        migrations.AddField(
            model_name='asset',
            name='assetgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb_api.AssetGroup'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='cmdb_api.IDC'),
        ),
        migrations.AddField(
            model_name='asset',
            name='usergroup',
            field=models.ManyToManyField(default=1, to='cmdb_api.UserGroup'),
        ),
    ]
