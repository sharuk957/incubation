# Generated by Django 3.2.6 on 2021-10-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incubation',
            name='Status',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
