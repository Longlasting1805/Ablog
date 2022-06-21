# Generated by Django 4.0.5 on 2022-06-21 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
