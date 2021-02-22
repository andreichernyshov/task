# Generated by Django 3.1.6 on 2021-02-13 03:39

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('data', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
    ]
