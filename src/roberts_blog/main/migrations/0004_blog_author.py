# Generated by Django 4.1.3 on 2022-11-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
