# Generated by Django 3.2.9 on 2021-12-02 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_avatar_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ('-date',)},
        ),
    ]
