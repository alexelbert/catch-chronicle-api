# Generated by Django 5.0.2 on 2024-02-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catches', '0004_rename_title_catch_caption_remove_catch_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catch',
            name='image',
            field=models.ImageField(default='../default_profile_zsweuz', upload_to='images/'),
        ),
    ]
