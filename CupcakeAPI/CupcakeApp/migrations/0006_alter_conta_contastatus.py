# Generated by Django 4.1.3 on 2022-11-18 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CupcakeApp', '0005_alter_conta_contanome_alter_conta_contatipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='ContaStatus',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
