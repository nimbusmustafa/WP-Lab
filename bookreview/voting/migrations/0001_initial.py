# Generated by Django 5.1.6 on 2025-03-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(choices=[('good', 'Good'), ('satisfactory', 'Satisfactory'), ('bad', 'Bad')], max_length=20)),
            ],
        ),
    ]
