# Generated by Django 4.1.7 on 2023-04-23 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='Price',
            new_name='Pricing',
        ),
    ]