# Generated by Django 5.0.7 on 2024-08-06 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agthi', '0009_subscriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('description1', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Latest_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Our_people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word_from_CEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
