# Generated by Django 4.1.5 on 2023-02-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255, verbose_name='comment')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
