# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', image_cropping.fields.ImageCropField(upload_to='')),
                ('cropping', image_cropping.fields.ImageRatioField('avatar', '360x360', size_warning=False, allow_fullsize=False, hide_image_field=False, help_text=None, verbose_name='cropping', free_crop=False, adapt_rotation=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
