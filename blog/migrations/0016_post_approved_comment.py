# Generated by Django 2.2.9 on 2020-01-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200128_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
