# Generated by Django 4.0.3 on 2022-03-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_mgmt', '0007_address_dateadded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='name',
        ),
        migrations.AddField(
            model_name='issue',
            name='title',
            field=models.CharField(default='ee', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(default='aaa', max_length=200),
            preserve_default=False,
        ),
    ]