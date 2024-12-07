# Generated by Django 5.1.4 on 2024-12-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=150)),
                ('joining_date', models.DateField()),
                ('educational_background', models.JSONField(blank=True)),
                ('salary', models.FloatField()),
            ],
        ),
    ]