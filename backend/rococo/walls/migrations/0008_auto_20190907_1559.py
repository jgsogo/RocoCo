# Generated by Django 2.2.5 on 2019-09-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walls', '0007_auto_20190907_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repetition',
            name='rep1',
            field=models.IntegerField(blank=True, choices=[(0, 'Pie libre'), (1, 'Pie mano')], null=True),
        ),
        migrations.AlterField(
            model_name='repetition',
            name='rep2',
            field=models.IntegerField(blank=True, choices=[(0, 'A vista'), (1, 'Flash')], null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='presas',
            field=models.ManyToManyField(blank=True, through='walls.PresaCatch', to='walls.Presa'),
        ),
        migrations.AlterField(
            model_name='route',
            name='seguros',
            field=models.ManyToManyField(blank=True, to='walls.Seguro'),
        ),
    ]
