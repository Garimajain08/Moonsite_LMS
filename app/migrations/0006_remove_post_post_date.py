# Generated by Django 4.2.6 on 2023-10-28 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_post_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_date',
        ),
    ]