# Generated by Django 5.0.7 on 2024-07-30 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TreeApp', '0006_alter_menuobject_parent_optional__and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuobject',
            old_name='Parent (optional)',
            new_name='line_parent',
        ),
        migrations.RenameField(
            model_name='menuobject',
            old_name='URL (optional)',
            new_name='line_url',
        ),
    ]
