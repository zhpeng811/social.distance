# Generated by Django 3.2.7 on 2021-09-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0005_auto_20210928_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_authors_author_friends_+', to='authors.Author'),
        ),
    ]
