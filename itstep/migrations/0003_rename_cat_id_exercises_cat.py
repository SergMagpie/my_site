# Generated by Django 3.2.4 on 2021-06-13 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itstep', '0002_auto_20210613_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercises',
            old_name='cat_id',
            new_name='cat',
        ),
    ]