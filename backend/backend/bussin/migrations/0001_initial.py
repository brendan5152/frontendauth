# Generated by Django 4.1.2 on 2022-10-27 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('kvk', models.IntegerField(max_length=100)),
                ('valid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('tag_status', models.CharField(choices=[('Eigenaar', 'Eigenaar'), ('Manager', 'Manager'), ('Promoter', 'Promoter')], default='Feestganger', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('street_address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('organisation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bussin.organisation')),
            ],
        ),
    ]
