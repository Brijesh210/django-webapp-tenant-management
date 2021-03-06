# Generated by Django 4.0.3 on 2022-03-10 21:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='dateAdded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='zipCode',
            field=models.CharField(max_length=15),
        ),
    ]
