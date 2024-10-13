# Generated by Django 5.1.2 on 2024-10-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentManagementPortal', '0006_remove_article_transcript_article_thumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessgroup',
            name='permissions_description',
            field=models.CharField(default='No permiddion data available', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accessgroup',
            name='group_name',
            field=models.CharField(max_length=400, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
