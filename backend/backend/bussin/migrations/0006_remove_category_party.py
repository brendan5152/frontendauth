# Generated by Django 4.1.2 on 2022-10-31 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bussin', '0005_remove_category_party_category_party'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='party',
        ),
    ]
