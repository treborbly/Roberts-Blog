# Generated by Django 4.1.3 on 2022-11-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_blog_author_alter_blog_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='no_image', upload_to='main/files'),
        ),
    ]
