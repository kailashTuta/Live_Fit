# Generated by Django 4.0.2 on 2022-04-19 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AyurvedicTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('image', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
    ]