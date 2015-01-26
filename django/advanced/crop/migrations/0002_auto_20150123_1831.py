# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('avatar', '200x200', verbose_name='cropping', help_text=None, adapt_rotation=False, size_warning=False, free_crop=False, hide_image_field=False, allow_fullsize=False),
            preserve_default=True,
        ),
    ]
