#Os modelos são as definições de quais dados existem em cada entidade, bem como
#seus respectivos tipos e tamanhos.

from django.db import models

#Modelo para os dados da entidade Conta.
#Contas são os usuários da aplicação.
class Conta (models.Model):
        ContaId = models.AutoField(primary_key=True) #Gerado automaticamente
        ContaNome = models.CharField(max_length=30, blank=True, default='') #Opcional
        ContaTipo = models.IntegerField(blank=True, null=True) #Opcional
        ContaRua = models.CharField(max_length=100, blank=True, default='') #Opcional
        ContaBairro = models.CharField(max_length=100, blank=True, default='') #Opcional
        ContaNumero = models.CharField(max_length=4, blank=True, default='') #Opcional
        ContaComplemento = models.CharField(max_length=4, blank=True, default='') #Opcional
        ContaCep = models.CharField(max_length=8, blank=True, default='') #Opcional
        ContaSenha = models.CharField(max_length=10) #Obrigatório
        ContaEmail = models.CharField(max_length=100) #Obrigatório
        ContaStatus = models.IntegerField(blank=True, null=True) #Opcional

#Modelo para os dados da entidade Cardapio;
#Essa é uma entidade intermediária que conecta uma conta com um produto.
#Ou seja, ela define os produtos que uma conta tem.
class Cardapio (models.Model):
        CardapioId = models.AutoField(primary_key=True)
        CardapioUsuario = models.ForeignKey("Conta", on_delete=models.CASCADE, default='')
        CardapioProduto = models.ForeignKey("Produto", on_delete=models.CASCADE, default='')

#Modelo para os dados da entidade Produto.
#São os produtos vendidos.
class Produto (models.Model):
        ProdutoId = models.AutoField(primary_key=True)
        ProdutoNome = models.CharField(max_length=30, blank=True, default='')
        ProdutoDescricao = models.CharField(max_length=100, blank=True, default='')
        ProdutoPreco = models.IntegerField(blank=True, null=True)
        ProdutoQuantidade= models.IntegerField(blank=True, null=True)

#Modelo para os dados da entidade Produto do Carrinho
#Produtos do carrinho são os produtos que serão emitidos em um pedido.
#Ou seja, são os produtos que o usuário escolheu comprar.
class ProdutoDoCarrinho (models.Model):
        ProdutoDoCarrinhoId = models.AutoField(primary_key=True)
        ProdutoDoCarrinhoNome = models.CharField(max_length=30, blank=True, default='')
        ProdutoDoCarrinhoPreco = models.IntegerField(blank=True, null=True)
        ProdutoDoCarrinhoQuantidade = models.IntegerField()
        ProdutoDoCarrinhoUsuario = models.ForeignKey("Conta", on_delete=models.CASCADE, default='')
        ProdutoDoCarrinhoProduto = models.ForeignKey("Produto", on_delete=models.CASCADE, default='')