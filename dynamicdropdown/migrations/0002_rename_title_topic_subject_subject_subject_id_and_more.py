# Generated by Django 4.0.5 on 2022-06-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicdropdown', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='title',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_id',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
