# Generated by Django 4.2.4 on 2023-09-08 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0040_alter_comment_pub_date_alter_note_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 18, 44, 1, 848795, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='note',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 18, 44, 1, 847808, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]