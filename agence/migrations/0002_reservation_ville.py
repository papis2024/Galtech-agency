# Generated by Django 4.2.4 on 2023-11-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='ville',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ville'),
        ),
    ]
