# Generated by Django 3.1.1 on 2020-12-05 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201205_0139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_upload',
            old_name='catergory',
            new_name='category',
        ),
    ]
