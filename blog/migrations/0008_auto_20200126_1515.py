# Generated by Django 2.2.9 on 2020-01-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200125_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='userwallet',
            field=models.CharField(default=5000, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
