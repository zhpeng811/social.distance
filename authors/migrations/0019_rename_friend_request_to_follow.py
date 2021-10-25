# Generated by Django 3.2.7 on 2021-10-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0018_auto_20211019_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='object',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follower',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='followee',
            new_name='object',
        ),
        migrations.AddField(
            model_name='follow',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted')], default='PENDING', max_length=20),
        ),
        migrations.AddField(
            model_name='follow',
            name='summary',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('object', 'actor'), name='unique_follower'),
        ),
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]
