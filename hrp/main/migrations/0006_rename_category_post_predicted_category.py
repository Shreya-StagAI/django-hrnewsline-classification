# Generated by Django 5.0.6 on 2024-06-02 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_predicted_category_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='predicted_category',
        ),
    ]