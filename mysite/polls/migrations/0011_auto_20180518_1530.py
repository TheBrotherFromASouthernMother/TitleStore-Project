# Generated by Django 2.0.5 on 2018-05-18 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20180518_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='cu_id_type',
            new_name='cu_photo_id_type',
        ),
    ]