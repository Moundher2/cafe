# Generated by Django 4.2.3 on 2023-08-02 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='buyermail',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='buyer',
            old_name='buyername',
            new_name='name',
        ),
    ]