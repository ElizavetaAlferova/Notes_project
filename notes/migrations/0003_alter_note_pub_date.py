# Generated by Django 4.2.4 on 2023-09-04 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 4, 9, 46, 38, 2864, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]