# Generated by Django 4.0.4 on 2022-05-27 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_192015', '0005_post_field_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='field_name',
            new_name='files',
        ),
    ]
