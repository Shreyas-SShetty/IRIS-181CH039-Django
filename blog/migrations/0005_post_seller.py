# Generated by Django 2.2.9 on 2020-01-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='seller',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]