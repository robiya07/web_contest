# Generated by Django 4.2.2 on 2023-07-11 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_alter_resultmodel_table_alter_surveymodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveymodel',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]