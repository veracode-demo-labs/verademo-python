# Generated by Django 4.2.13 on 2024-06-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_user_datecreated_user_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='blabName',
            new_name='blab_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastLogin',
            new_name='last_login',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='realName',
            new_name='real_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
