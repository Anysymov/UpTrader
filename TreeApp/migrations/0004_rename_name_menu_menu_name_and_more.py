# Generated by Django 5.0.7 on 2024-07-30 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TreeApp', '0003_alter_menuobject_parent_optional__and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='menu_name',
        ),
        migrations.RenameField(
            model_name='menuobject',
            old_name='name',
            new_name='line_name',
        ),
        migrations.RenameField(
            model_name='menuobject',
            old_name='menu',
            new_name='menu_name',
        ),
    ]