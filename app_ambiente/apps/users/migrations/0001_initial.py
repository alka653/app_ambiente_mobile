# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('foto', models.ImageField(default=b'img/users/none.png', upload_to=b'img/users/', blank=True)),
                ('numero_celular', models.CharField(max_length=10, null=True, blank=True)),
                ('direccion', models.CharField(max_length=40, null=True, blank=True)),
                ('key_user', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
