# Generated by Django 2.1.4 on 2019-02-06 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190206_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='l_name',
            new_name='last_name',
        ),
    ]
