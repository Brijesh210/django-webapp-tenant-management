# Generated by Django 4.0.3 on 2022-03-13 20:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_mgmt', '0008_remove_issue_name_issue_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuecategory',
            name='dateAdded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('CRE', 'Created'), ('ASS', 'Assigned'), ('PRO', 'In Progress'), ('COM', 'Completed'), ('DEL', 'Deleted'), ('CLO', 'Closed')], default='CRE', max_length=3),
        ),
    ]
