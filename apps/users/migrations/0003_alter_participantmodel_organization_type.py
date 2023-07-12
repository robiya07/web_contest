# Generated by Django 4.2.2 on 2023-07-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_organization_remove_participantmodel_kindergarten_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantmodel',
            name='organization_type',
            field=models.CharField(choices=[('school', 'Школа'), ('kindergarten', 'Детский сад'), ('other', 'Другое')], default='school', max_length=15),
        ),
    ]
