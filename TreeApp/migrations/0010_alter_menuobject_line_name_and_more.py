# Generated by Django 5.0.7 on 2024-08-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TreeApp', '0009_alter_menu_menu_name_alter_menuobject_line_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuobject',
            name='line_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddConstraint(
            model_name='menuobject',
            constraint=models.UniqueConstraint(fields=('line_name', 'menu_name'), name='unique_name_and_menu'),
        ),
    ]