# Generated by Django 4.0.4 on 2022-05-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_192015', '0004_rename_blogpost_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='field_name',
            field=models.FileField(max_length=254, null=True, upload_to=None),
        ),
    ]