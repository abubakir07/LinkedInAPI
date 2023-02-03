# Generated by Django 4.1.5 on 2023-02-03 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=500)),
                ('files', models.FileField(blank=True, upload_to='', verbose_name='files')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create_at')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='chats.chat', verbose_name='chat id')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'Messages',
                'ordering': ('-create_at',),
            },
        ),
    ]