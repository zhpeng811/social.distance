# Generated by Django 3.2.7 on 2021-10-03 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_update_related_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('PUB', 'PUBLIC'), ('FRI', 'FRIENDS'), ('PRI', 'PRIVATE')], default='PUB', max_length=3),
        ),
    ]
