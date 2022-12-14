# Generated by Django 4.1.3 on 2022-11-17 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('CardapioId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('ContaId', models.AutoField(primary_key=True, serialize=False)),
                ('ContaNome', models.CharField(max_length=30)),
                ('ContaTipo', models.IntegerField(max_length=1)),
                ('ContaRua', models.CharField(max_length=100)),
                ('ContaBairro', models.CharField(max_length=100)),
                ('ContaNumero', models.CharField(max_length=4)),
                ('ContaComplemento', models.CharField(max_length=4)),
                ('ContaCep', models.CharField(max_length=8)),
                ('ContaSenha', models.CharField(max_length=10)),
                ('ContaEmail', models.CharField(max_length=20)),
                ('ContaStatus', models.CharField(max_length=1)),
                ('ContaCardapio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CupcakeApp.cardapio')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('ProdutoId', models.AutoField(primary_key=True, serialize=False)),
                ('ProdutoNome', models.CharField(max_length=30)),
                ('ProdutoDescricao', models.CharField(max_length=100)),
                ('ProdutoPreco', models.IntegerField(max_length=4)),
                ('ProdutoQuantidade', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoDoCarrinho',
            fields=[
                ('ProdutoDoCarrinhoId', models.AutoField(primary_key=True, serialize=False)),
                ('ProdutoDoCarrinhoQuantidade', models.IntegerField(max_length=4)),
                ('ProdutoDoCarrinhoProduto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CupcakeApp.produto')),
                ('ProdutoDoCarrinhoUsuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CupcakeApp.conta')),
            ],
        ),
        migrations.AddField(
            model_name='cardapio',
            name='CardapioProduto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CupcakeApp.produto'),
        ),
    ]
