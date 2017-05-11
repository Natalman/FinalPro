# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 16:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Trainer', '0009_auto_20170511_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatroom',
            old_name='name',
            new_name='message',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatroom',
            name='user',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
