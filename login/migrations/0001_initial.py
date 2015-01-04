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
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line1', models.CharField(default=b'asfdf', max_length=200)),
                ('line2', models.CharField(default=b'asfdf', max_length=200)),
                ('city', models.CharField(default=b'asfdf', max_length=50)),
                ('state', models.CharField(default=b'asfdf', max_length=50)),
                ('pin', models.CharField(default=b'asfdf', max_length=10)),
                ('landmark', models.CharField(default=b'asfdf', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(default=b'asfdf', max_length=11)),
                ('address', models.ForeignKey(to='login.Address')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
