# Generated by Django 5.1 on 2024-09-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_author_task_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
