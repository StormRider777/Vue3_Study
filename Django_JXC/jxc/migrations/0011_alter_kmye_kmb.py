# Generated by Django 4.0.3 on 2022-12-24 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jxc', '0010_alter_kmye_kmb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kmye',
            name='kmb',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jxc.kmb'),
        ),
    ]
