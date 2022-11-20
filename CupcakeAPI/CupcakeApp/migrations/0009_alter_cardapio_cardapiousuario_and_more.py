# Generated by Django 4.1.3 on 2022-11-20 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CupcakeApp', '0008_produtodocarrinho_produtodocarrinhopreco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='CardapioUsuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CupcakeApp.conta'),
        ),
        migrations.AlterField(
            model_name='produtodocarrinho',
            name='ProdutoDoCarrinhoUsuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CupcakeApp.conta'),
        ),
    ]
