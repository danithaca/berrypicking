# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignment_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('worker_id', models.CharField(max_length=14)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssignmentSurvey',
            fields=[
                ('assignment', models.OneToOneField(serialize=False, db_column='assignment_id', primary_key=True, to='mturk.Assignment')),
                ('category', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssignmentTranslation',
            fields=[
                ('assignment', models.OneToOneField(serialize=False, db_column='assignment_id', primary_key=True, to='mturk.Assignment')),
                ('translated', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HIT',
            fields=[
                ('hit_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('hit_type_id', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HITSurvey',
            fields=[
                ('hit', models.OneToOneField(serialize=False, db_column='hit_id', primary_key=True, to='mturk.HIT')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HITTranslation',
            fields=[
                ('hit', models.OneToOneField(serialize=False, db_column='hit_id', primary_key=True, to='mturk.HIT')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('ref', models.IntegerField(primary_key=True, serialize=False)),
                ('feedback', models.TextField()),
                ('language_code', models.CharField(max_length=2, blank=True)),
                ('gtrans', models.TextField(blank=True)),
                ('turk1', models.TextField(blank=True)),
                ('turk2', models.TextField(blank=True)),
                ('categorization_result', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hittranslation',
            name='survey',
            field=models.ForeignKey(to='mturk.Survey'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hitsurvey',
            name='survey',
            field=models.ForeignKey(to='mturk.Survey'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='hit',
            field=models.ForeignKey(db_column='hit_id', to='mturk.HIT'),
            preserve_default=True,
        ),
    ]
