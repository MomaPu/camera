# Generated by Django 5.2 on 2025-04-18 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0004_remove_session_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='session_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scan.session'),
        ),
    ]
