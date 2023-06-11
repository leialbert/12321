# Generated by Django 4.2.2 on 2023-06-11 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0003_requestlog_remove_phonenumber_tags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlog',
            name='callId',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Call ID'),
            preserve_default=False,
        ),
    ]
