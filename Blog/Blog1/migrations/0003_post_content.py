# Generated by Django 4.0.3 on 2023-03-06 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog1', '0002_alter_post_options_post_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
