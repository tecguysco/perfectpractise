# Generated by Django 2.0 on 2018-05-18 10:00

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('constant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeltaShotReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('distance', models.PositiveIntegerField()),
                ('delta', django.contrib.postgres.fields.jsonb.JSONField(help_text='Delta and Advanced Shot Reporting')),
                ('hit', models.PositiveSmallIntegerField(choices=[(1, 'Hit'), (0, 'Miss')], default=0)),
                ('aim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constant.AimValueRange')),
            ],
            options={
                'ordering': ('practice', 'reported_at'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_type', models.PositiveSmallIntegerField(choices=[(10, 'Full Swing (Gated Random)'), (11, 'Serial'), (12, 'Block'), (13, 'Warmup'), (20, 'Gated Random Putting'), (21, 'Standard Putting'), (22, 'Within 3 Feet'), (23, '6 Foot Challenge'), (30, 'Around the green (Chip)'), (31, 'Around the green (Pitch)')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='practices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ScoreShotReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('distance', models.PositiveIntegerField(blank=True, null=True)),
                ('putt_counts', models.PositiveSmallIntegerField(help_text='putt counts required')),
                ('points', models.IntegerField()),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Practice')),
            ],
            options={
                'ordering': ('practice', 'reported_at'),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='deltashotreport',
            name='practice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Practice'),
        ),
        migrations.AddField(
            model_name='deltashotreport',
            name='trajectory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constant.TrajectoryValueRange'),
        ),
    ]