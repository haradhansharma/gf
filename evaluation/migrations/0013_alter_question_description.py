# Generated by Django 4.0.1 on 2022-02-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0012_question_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(),
        ),
    ]
