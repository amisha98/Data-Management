# Generated by Django 2.1.1 on 2018-10-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_id',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
