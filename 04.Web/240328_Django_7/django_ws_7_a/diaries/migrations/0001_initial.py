# Generated by Django 4.2.9 on 2024-03-29 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=125)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]