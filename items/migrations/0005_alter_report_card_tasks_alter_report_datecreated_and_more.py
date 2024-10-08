# Generated by Django 5.1 on 2024-08-27 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_user_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='card_tasks',
            field=models.ManyToManyField(to='items.cardtask'),
        ),
        migrations.AlterField(
            model_name='report',
            name='dateCreated',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='report',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.user'),
        ),
    ]
