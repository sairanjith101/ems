# Generated by Django 5.1 on 2024-08-27 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_leaverequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager_requests', to='main.employee'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='processed_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='tl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tl_requests', to='main.employee'),
        ),
    ]
