# Generated by Django 5.0.3 on 2024-03-30 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_alter_unitmenu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermeallike',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
