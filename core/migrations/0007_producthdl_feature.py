# Generated by Django 3.2.3 on 2021-10-28 14:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_about_title_ar'),
    ]

    operations = [
        migrations.AddField(
            model_name='producthdl',
            name='feature',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
