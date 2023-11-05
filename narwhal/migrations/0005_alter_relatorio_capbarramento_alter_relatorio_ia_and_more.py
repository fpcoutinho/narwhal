# Generated by Django 4.2.7 on 2023-11-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('narwhal', '0004_alter_circuito_condutor_alter_circuito_corrente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorio',
            name='capbarramento',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='ia',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='ib',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='ic',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='protdps',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='protdr',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='protgeral',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='vab',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='van',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='vbc',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='vbn',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='vca',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='vcn',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
    ]