# Generated by Django 3.1.2 on 2020-10-30 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRole',
            new_name='AssociatedPeroon',
        ),
    ]
