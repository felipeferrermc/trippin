# Generated by Django 4.2.7 on 2023-11-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_rename_location_category_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
