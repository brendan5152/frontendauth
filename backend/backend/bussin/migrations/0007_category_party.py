# Generated by Django 4.1.2 on 2022-10-31 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bussin', '0006_remove_category_party'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='party',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bussin.party'),
            preserve_default=False,
        ),
    ]
