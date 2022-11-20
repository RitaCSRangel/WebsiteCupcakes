#Arquivo que permite a transformação dos tipos de data complexo que são
#os models em tipos de dado manejáveis pelo Python e vice-versa

from rest_framework import serializers
from CupcakeApp.models import Conta, Cardapio, Produto, ProdutoDoCarrinho

#Serializer do model da entidade de Conta
class ContaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = (
            'ContaId',
            'ContaNome',
            'ContaTipo',
            'ContaRua',
            'ContaBairro',
            'ContaNumero',
            'ContaComplemento',
            'ContaCep',
            'ContaSenha',
            'ContaEmail',
            'ContaStatus'
        )

#Serializer do model da entidade de Cardapio
class CardapioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        fields = (
            'CardapioId',
            'CardapioUsuario',
            'CardapioProduto'
        )

#Serializer do model da entidade de Produto
class ProdutoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'ProdutoId',
            'ProdutoNome',
            'ProdutoDescricao',
            'ProdutoPreco',
            'ProdutoQuantidade'
        )

#Serializer do model da entidade de ProdutoDoCarrinho
class ProdutoDoCarrinhoSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProdutoDoCarrinho
        fields = (
            'ProdutoDoCarrinhoId',
            'ProdutoDoCarrinhoQuantidade',
            'ProdutoDoCarrinhoUsuario',
            'ProdutoDoCarrinhoProduto'
        )