# Generated by Django 3.1.3 on 2020-11-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_thumb',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
