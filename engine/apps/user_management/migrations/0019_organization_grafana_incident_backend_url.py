# Generated by Django 4.2.7 on 2023-11-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0018_auto_20231115_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='grafana_incident_backend_url',
            field=models.CharField(default=None, max_length=300, null=True),
        ),
    ]