# Generated by Django 3.2.7 on 2021-09-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0006_alter_author_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='github_url',
            field=models.URLField(null=True),
        ),
    ]