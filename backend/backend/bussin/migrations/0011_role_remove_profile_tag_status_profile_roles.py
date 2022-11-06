# Generated by Django 4.1.3 on 2022-11-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussin', '0010_alter_category_party'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'teacher'), (3, 'secretary'), (4, 'supervisor'), (5, 'admin')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tag_status',
        ),
        migrations.AddField(
            model_name='profile',
            name='roles',
            field=models.ManyToManyField(to='bussin.role'),
        ),
    ]
