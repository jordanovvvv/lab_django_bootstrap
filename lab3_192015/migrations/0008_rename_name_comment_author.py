# Generated by Django 4.0.4 on 2022-05-28 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_192015', '0007_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author',
        ),
    ]