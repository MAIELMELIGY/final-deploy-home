# Generated by Django 3.2.3 on 2021-10-27 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211027_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mision_vision',
            name='icon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]