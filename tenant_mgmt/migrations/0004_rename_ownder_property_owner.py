# Generated by Django 4.0.3 on 2022-03-10 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_mgmt', '0003_rename_ownerid_property_ownder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='ownder',
            new_name='owner',
        ),
    ]
