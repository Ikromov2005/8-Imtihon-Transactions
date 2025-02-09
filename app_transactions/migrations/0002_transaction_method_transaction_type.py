# Generated by Django 5.0.6 on 2024-06-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='method',
            field=models.CharField(choices=[('card', 'Kartadan'), ('cash', 'Naqd pul'), ('click', 'Click')], default='income', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('income', 'Kirim'), ('expense', 'Chiqim')], default='card', max_length=7),
            preserve_default=False,
        ),
    ]
