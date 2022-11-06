# Generated by Django 4.1.2 on 2022-10-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussin', '0003_party'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='kvk',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('ordinal', models.IntegerField()),
                ('party', models.ManyToManyField(to='bussin.party')),
            ],
        ),
    ]