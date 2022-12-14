# Generated by Django 4.0.3 on 2022-12-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jxc', '0011_alter_kmye_kmb'),
    ]

    operations = [
        migrations.AddField(
            model_name='kmb',
            name='dfje',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='贷方金额'),
        ),
        migrations.AddField(
            model_name='kmb',
            name='dfsl',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=15, verbose_name='贷方数量'),
        ),
        migrations.AddField(
            model_name='kmb',
            name='jfje',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='借方金额'),
        ),
        migrations.AddField(
            model_name='kmb',
            name='jfsl',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=15, verbose_name='借方数量'),
        ),
        migrations.AddField(
            model_name='kmb',
            name='qcje',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='期初金额'),
        ),
        migrations.AddField(
            model_name='kmb',
            name='qcsl',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=15, verbose_name='期初数量'),
        ),
        migrations.AddField(
            model_name='kmb',
            name='qmje',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='期末金额'),
        ),
        migrations.AddField(
            model_name='kmb',
            name='qmsl',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=15, verbose_name='期末数量'),
        ),
        migrations.DeleteModel(
            name='Kmye',
        ),
    ]
