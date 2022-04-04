# Generated by Django 4.0.2 on 2022-04-04 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=100)),
                ('equipment', models.CharField(max_length=100)),
                ('exercise_type', models.CharField(max_length=100)),
                ('major_muscle', models.CharField(max_length=100)),
                ('minor_muscle', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('example', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('notes', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('modification', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
    ]
