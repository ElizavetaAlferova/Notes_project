# Generated by Django 4.2.4 on 2023-09-05 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0016_note_pdf_alter_comment_pub_date_alter_note_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 11, 48, 15, 823721, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='note',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 5, 11, 48, 15, 822718, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
