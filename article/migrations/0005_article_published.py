# Generated by Django 4.1 on 2022-09-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_timestamp_article_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.DateField(null=True),
        ),
    ]
