# Generated by Django 4.2.2 on 2023-07-11 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_participantmodel_organization_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantmodel',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='users.organization'),
        ),
    ]
