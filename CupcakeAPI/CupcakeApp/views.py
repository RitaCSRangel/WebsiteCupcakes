#É nesse arquivo que são definidos os métodos de API para utilização dos dados
#contidos nas entidades deste DB.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #Permitir outros domínios acessarem esses métodos
from rest_framework.parsers import JSONParser #Transformar o dado recebido em DataModel
from django.http.response import JsonResponse #Enviar dados de resposta da API

from CupcakeApp.models import Conta, Cardapio, Produto, ProdutoDoCarrinho
from CupcakeApp.serializer import ContaSerializer, CardapioSerializer, ProdutoSerializer, ProdutoDoCarrinhoSerializer

from django.core.files.storage import default_storage
from django_filters.rest_framework import DjangoFilterBackend

filter_backends = [DjangoFilterBackend]
filterset_fields = ['CardapioUsuario']

@csrf_exempt
def ContaApi (request, id=0):

    #Buscar todas as contas
    if request.method=='GET':
        contas = Conta.objects.all() #Obter todos os registros da entidade
        contas_serializer = ContaSerializer(contas, many=True)  #Transformar esses dados obtidos complexos em dados legíveis
        return JsonResponse(
            {
                'Code':200,
                'Objeto': contas_serializer.data
            }
        ) #Retorna um sucesso   
    
    #Criar uma nova conta
    elif request.method=='POST':
        conta_data = JSONParser().parse(request) #Dar um parse no dado recebido
        conta_serializer = ContaSerializer(data=conta_data) #Converter o dado recebido em um dado mais completo que o model entenda
        if conta_serializer.is_valid(): #Se esse dado formar um model válido
            conta_serializer.save() #Salva no banco
            return JsonResponse(
                {
                    'Code':200,
                    'Message': 'Conta registrada com sucesso'
                }
            ) #Retorna um sucesso              
        return JsonResponse(
            {
                'Code':400,
                'Message': 'Falha ao registrar conta: ' + str(conta_serializer.errors)
            }
        ) #Retorna uma falha

    #Alterar uma conta
    elif request.method=='PUT':
        conta_data = JSONParser().parse(request) #Dar um parse no dado recebido
        contaExistente = Conta.objects.get(ContaId=conta_data['ContaId']) #Obter o registro que corresponde ao ID recebido
        conta_serializer = ContaSerializer(contaExistente, data=conta_data) #Converter o dado recebido em um dado mais completo que o model entenda, utilizando como base o registro encontrado
        if conta_serializer.is_valid(): #Se esse dado formar um model válido
            conta_serializer.save() #Salva no banco
            return JsonResponse(
                {
                    'Code':200,
                    'Message': 'Conta atualizada com sucesso'
                }
            ) #Retorna um sucesso              
        return JsonResponse(
            {
                'Code':400,
                'Message': 'Falha ao atualizar conta: ' + str(conta_serializer.errors)
            }
        ) #Retorna uma falha

    #Deletar uma conta
    elif request.method=='DELETE':
        contaExistente = Conta.objects.filter(ContaId=id) #Obter o registro que corresponde ao ID recebido
        contaExistente.delete() #Deletar o registro encontrado
        return JsonResponse(
            {
                'Code':200,
                'Message': 'Conta atualizada com sucesso'
            }
        ) #Retorna um sucesso              

@csrf_exempt
def LoginUsuarioApi (request):

    #Buscar um usuário através de e-mail e senha
    if request.method=='POST':
        conta_data = JSONParser().parse(request) #Dar um parse no dado recebido
        contaExistente = Conta.objects.get(ContaEmail=conta_data['ContaEmail'], ContaSenha=conta_data['ContaSenha']) #Obter o registro que corresponde ao Email e Senha recebidos
        conta_serializer = ContaSerializer(contaExistente, data=conta_data) #Converter o dado recebido em um dado mais completo que o model entenda
        if conta_serializer.is_valid(): #Se esse dado formar um model válido
            return JsonResponse(
                {
                    'Code':200,
                    'Message': 'Login realizado com sucesso',
                    'Objeto': conta_serializer.data
                }
            ) #Retorna um sucesso              
        return JsonResponse(
            {
                'Code':400,
                'Message': 'Falha ao logar conta: ' + str(conta_serializer.errors)
            }
        ) #Retorna uma falha

@csrf_exempt
def CardapioApi (request, id=0):

    #Obter todos os cardápios
    if request.method=='GET':
        cardapio_data = JSONParser().parse(request) #Dar um parse no dado recebido
        cardapio = Cardapio.objects.all(CardapioUsuario=cardapio_data['CardapioUsuario']) #Obter o registro que corresponde ao ID recebido
        if cardapio!=None:
            cardapio_filter = Cardapio.objects.all(CardapioUsuario=cardapio_data['CardapioUsuario'])  #Transformar esses dados obtidos complexos em dados legíveis
            return JsonResponse(
                {
                    'Code':200,
                    'Objeto': cardapio_serializer.data
                }
            ) #Retorna um sucesso   
    
    #Criar um novo cardápio
    elif request.method=='POST':
        cardapio_data = JSONParser().parse(request) #Dar um parse no dado recebido
        cardapio_serializer = CardapioSerializer(data=cardapio_data) #Converter o dado recebido em um dado mais completo que o model entenda
        if cardapio_serializer.is_valid(): #Se esse dado formar um model válido
            cardapio_serializer.save() #Salva no banco
            return JsonResponse(
                {
                    'Code':200,
                    'Message': 'Cardapio registrado com sucesso'
                }
            ) #Retorna um sucesso              
        return JsonResponse(
            {
                'Code':400,
                'Message': 'Falha ao registrar cardapio: ' + str(cardapio_serializer.errors)
            }
        ) #Retorna uma falha

    #Alterar um cardápio
    elif request.method=='PUT':
        cardapio_data = JSONParser().parse(request) #Dar um parse no dado recebido
        cardapioExistente = Cardapio.objects.get(CardapioId=cardapio_data['CardapioId']) #Obter o registro que corresponde ao ID recebido
        cardapio_serializer = CardapioSerializer(cardapioExistente, data=cardapio_data) #Converter o dado recebido em um dado mais completo que o model entenda, utilizando como base o registro encontrado
        if cardapio_serializer.is_valid(): #Se esse dado formar um model válido
            cardapio_serializer.save() #Salva no banco
            return JsonResponse(
                {
                    'Code':200,
                    'Message': 'Cardapio atualizado com sucesso'
                }
            ) #Retorna um sucesso              
        return JsonResponse(
            {
                'Code':400,
                'Message': 'Falha ao atualizar cardapio: ' + str(cardapio_serializer.errors)
            }
        ) #Retorna uma falha

    #Deletar um cardápio
    elif request.method=='DELETE':
        cardapioExistente = Cardapio.objects.filter(CardapioId=id) #Obter o registro que corresponde ao ID recebido
        cardapioExistente.delete() #Deletar o registro encontrado
        return JsonResponse(
            {
                'Code':200,
                'Message': 'Cardapio deletado com sucesso'
            }
        ) #Retorna um sucesso              

@csrf_exempt
def ObterCardapioPorUsuarioApi (request):

    #Obter os cardápios de um usuário específico
    if request.method=='GET':
        cardapio = Cardapio.objects.get() #Obter todos os registros da entidade



@csrf_exempt
def ProdutosDoCardapioApi (request):

    if request.method=='POST':
        produtoDoCardapio_data = JSONParser().parse(request) #Dar um parse no dado recebido
        produtoDoCardapioExistente = Produto.objects.get(ProdutoId=produtoDoCardapio_data['ProdutoId']) #Obter o registro que corresponde id de produto recebidos
        produtoDoCardapio_serializer = ProdutoSerializer(produtoDoCardapioExistente, data=produtoDoCardapio_data) #Converter o dado recebido em um dado mais completo que o model entenda
        if produtoDoCardapio_serializer.is_valid(): #Se esse dado formar um model válido
            return JsonResponse(
                {
                    'Code':200,
                    'Message': 'Produtos do cardapio obtidos com sucesso',
                    'Objeto': produtoDoCardapio_serializer.data
                }
            ) #Retorna um sucesso              
        return JsonResponse(
            {
                'Code':400,
                'Message': 'Falha ao obter produtos do cardapio: ' + str(produtoDoCardapio_serializer.errors)
            }
        ) #Retorna uma falha


@csrf_exempt
def ProdutoApi (request, id=0):

    if request.method=='GET':
        produto = Produto.objects.all() #Obter todos os registros da entidade
        produto_serializer = ProdutoSerializer(produto, many=True)  #Transformar esses dados obtidos complexos em dados legíveis
        return JsonResponse(
            {
                'Code':200,
                'Objeto': produto_serializer.data
            }
        ) #Retorna um sucesso     

    elif request.method=='POST':
        produto_data = JSONParser().parse(request) #Dar um parse no dado recebido
        produto_serializer = ProdutoSerializer(data=produto_data) #Converter o dado recebido em um dado mais completo que o model entenda
        if produto_serializer.is_valid(): #Se esse dado formar um model válido
            produto_serializer.save() #Salva no banco
            return JsonResponse(
                {
                    'Code':200,
                    'Message': 'Produto registrado com sucesso'
                }
            ) #Retorna um sucesso              
        return JsonResponse(
            {
                'Code':400,
                'Message': 'Falha ao registrar produto: ' + str(produto_serializer.errors)
            }
        ) #Retorna uma falha

    elif request.method=='PUT':
        produto_data = JSONParser().parse(request) #Dar um parse no dado recebido
        produtoExistente = Produto.objects.get(ProdutoId=produto_data['ProdutoId']) #Obter o registro que corresponde ao ID recebido
        produto_serializer = ProdutoSerializer(produtoExistente, data=produto_data) #Converter o dado recebido em um dado mais completo que o model entenda, utilizando como base o registro encontrado
        if produto_serializer.is_valid(): #Se esse dado formar um model válido
            produto_serializer.save() #Salva no banco
            return JsonResponse(
                {
                    'Code':200,
                    'Message': 'Produto atualizado com sucesso'
                }
            ) #Retorna um sucesso              
        return JsonResponse(
            {
                'Code':400,
                'Message': 'Falha ao atualizar produto: ' + str(produto_serializer.errors)
            }
        ) #Retorna uma falha

    elif request.method=='DELETE':
        produtoExistente = Produto.objects.get(ProdutoId=id) #Obter o registro que corresponde ao ID recebido
        produtoExistente.delete() #Deletar o registro encontrado
        return JsonResponse(
            {
                'Code':200,
                'Message': 'Produto deletado com sucesso'
            }
        ) #Retorna um sucesso   

@csrf_exempt
def ProdutoDoCarrinhoDoCarrinhoApi (request, id=0):

    if request.method=='GET':
        produtodocarrinho = ProdutoDoCarrinho.objects.all() #Obter todos os registros da entidade
        produtodocarrinho_serializer = ProdutoDoCarrinhoSerializer(produtodocarrinho, many=True)  #Transformar esses dados obtidos complexos em dados legíveis
        return JsonResponse(
            {
                'Code':200,
                'Objeto': produtodocarrinho_serializer.data
            }
        ) #Retorna um sucesso  

    elif request.method=='POST':
        produtodocarrinho_data = JSONParser().parse(request) #Dar um parse no dado recebido
        produtodocarrinho_serializer = ProdutoDoCarrinhoSerializer(data=produtodocarrinho_data) #Converter o dado recebido em um dado mais completo que o model entenda
        if produtodocarrinho_serializer.is_valid(): #Se esse dado formar um model válido
            produtodocarrinho_serializer.save() #Salva no banco
            return JsonResponse(
                {
                    'Code':200,
                    'Message': 'Produto do Carrinho registrado com sucesso'
                }
            ) #Retorna um sucesso              
        return JsonResponse(
            {
                'Code':400,
                'Message': 'Falha ao registrar produto do carrinho: ' + str(produtodocarrinho_serializer.errors)
            }
        ) #Retorna uma falha

    elif request.method=='PUT':
        produtodocarrinho_data = JSONParser().parse(request) #Dar um parse no dado recebido
        produtodocarrinhoExistente = ProdutoDoCarrinho.objects.get(ProdutoDoCarrinhoId=produtodocarrinho_data['ProdutoDoCarrinhoId']) #Obter o registro que corresponde ao ID recebido
        produtodocarrinho_serializer = ProdutoDoCarrinhoSerializer(produtodocarrinhoExistente, data=produtodocarrinho_data) #Converter o dado recebido em um dado mais completo que o model entenda, utilizando como base o registro encontrado
        if produtodocarrinho_serializer.is_valid(): #Se esse dado formar um model válido
            produtodocarrinho_serializer.save() #Salva no banco
            return JsonResponse(
                {
                    'Code':200,
                    'Message': 'Produto do Carrinho alterado com sucesso'
                }
            ) #Retorna um sucesso              
        return JsonResponse(
            {
                'Code':400,
                'Message': 'Falha ao alterar produto do carrinho: ' + str(produtodocarrinho_serializer.errors)
            }
        ) #Retorna uma falha

    elif request.method=='DELETE':
        produtodocarrinhoExistente = ProdutoDoCarrinho.objects.get(ProdutoDoCarrinhoId=id) #Obter o registro que corresponde ao ID recebido
        produtodocarrinhoExistente.delete() #Deletar o registro encontrado
        return JsonResponse(
            {
                'Code':200,
                'Message': 'Produto do carrinho deletado com sucesso'
            }
        ) #Retorna um sucesso 

@csrf_exempt
def SaveFile (request):
    file = request.FILES['uploadedFile'] #Obter o arquivo revebido no request
    file_name = default_storage.save(file.name, file) #Salvar esse arquivo
    return JsonResponse(file_name, safe=False)
