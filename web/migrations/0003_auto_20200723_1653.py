# Generated by Django 3.0.8 on 2020-07-23 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Curso',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
