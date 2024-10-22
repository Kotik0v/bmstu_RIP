# Generated by Django 4.2.16 on 2024-10-15 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlowAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('formed_at', models.DateTimeField(blank=True, null=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
                ('day_time', models.CharField(max_length=50)),
                ('flow', models.FloatField()),
                ('moderator', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flow_analyses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=50)),
                ('picture_url', models.CharField(max_length=255)),
                ('line_number', models.IntegerField()),
                ('line_name', models.CharField(max_length=50)),
                ('line_color', models.CharField(max_length=7)),
                ('average_visits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FlowAnalysisStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('flow_analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='main.flowanalysis')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.station')),
            ],
            options={
                'unique_together': {('station', 'flow_analysis')},
            },
        ),
    ]
