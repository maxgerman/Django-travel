# Generated by Django 3.2 on 2021-05-30 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_city_options'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city_set', to='cities.city', verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='train',
            name='to_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city_set', to='cities.city', verbose_name='To'),
        ),
    ]