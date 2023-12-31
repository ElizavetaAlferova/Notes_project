# Generated by Django 4.2.4 on 2023-09-07 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0027_alter_comment_pub_date_alter_note_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='text',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 7, 13, 45, 40, 879122, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='note',
            name='pdf',
            field=models.FileField(blank=True, default=None, null=True, upload_to='df/'),
        ),
        migrations.AlterField(
            model_name='note',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 7, 13, 45, 40, 879122, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
