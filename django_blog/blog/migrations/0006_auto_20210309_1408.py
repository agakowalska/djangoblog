# Generated by Django 3.1.7 on 2021-03-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210309_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='post_title',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_title',
            field=models.CharField(max_length=250),
        ),
    ]