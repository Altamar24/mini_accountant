# Generated by Django 5.0.3 on 2024-04-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
