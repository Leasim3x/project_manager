# Generated by Django 5.0.2 on 2024-02-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_rename_date_complet_project_date_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]