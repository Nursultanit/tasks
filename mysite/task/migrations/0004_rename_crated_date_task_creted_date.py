# Generated by Django 5.0.7 on 2024-07-13 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_rename_creted_date_task_crated_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='crated_date',
            new_name='creted_date',
        ),
    ]
