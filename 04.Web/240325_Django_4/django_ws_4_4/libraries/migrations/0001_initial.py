# Generated by Django 4.2.2 on 2024-03-28 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Isbn', models.CharField(max_length=10)),
                ('Author', models.TextField()),
                ('Title', models.TextField()),
                ('Category_name', models.TextField()),
                ('Category_id', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Fixed_price', models.BooleanField()),
                ('Pub_date', models.DateField()),
            ],
        ),
    ]