# Generated by Django 4.0.4 on 2022-06-02 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_192015', '0008_rename_name_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
