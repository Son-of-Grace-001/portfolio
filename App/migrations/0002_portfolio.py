# Generated by Django 4.2.5 on 2023-09-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.TextField()),
                ('project_source_link', models.CharField(max_length=200)),
                ('project_link_code', models.CharField(max_length=200)),
                ('project_type', models.CharField(max_length=100)),
            ],
        ),
    ]
