# Generated by Django 4.0.3 on 2022-03-13 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_mgmt', '0011_rename_comments_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='assigner',
            new_name='manager',
        ),
    ]
