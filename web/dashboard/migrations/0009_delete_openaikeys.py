# Generated by Django 3.2.4 on 2023-07-28 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_merge_0007_netlasapikey_openaiapikey_0007_openaikeys'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OpenAIKeys',
        ),
    ]