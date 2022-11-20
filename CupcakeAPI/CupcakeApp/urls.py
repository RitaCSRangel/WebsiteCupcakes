#Nesse arquivo serão definidas as urls que serão usadas para chamar a API

from django.urls import re_path as url
from CupcakeApp import views

from django.conf.urls.static import static #Adicionando um caminho statico para conseguir acessar a pasta de medias
from django.conf import settings

urlpatterns=[
    url(r'^conta/$', views.ContaApi),
    url(r'^conta/([0-9]+)$', views.ContaApi),

    url(r'^auth/$', views.LoginUsuarioApi),
    url(r'^auth/([0-9]+)$', views.LoginUsuarioApi),

    url(r'^cardapio/$', views.CardapioApi),
    url(r'^cardapio/([0-9]+)$', views.CardapioApi),

    url(r'^cardapioUsuario/$', views.ObterCardapioPorUsuarioApi),
    url(r'^cardapioUsuario/([0-9]+)$', views.ObterCardapioPorUsuarioApi),

    url(r'^produtosCardapio/$', views.ProdutosDoCardapioApi),
    url(r'^produtosCardapio/([0-9]+)$', views.ProdutosDoCardapioApi),
    
    url(r'^produto/$', views.ProdutoApi),
    url(r'^produto/([0-9]+)$', views.ProdutoApi),

    url(r'^carrinho/$', views.ProdutoDoCarrinhoDoCarrinhoApi),
    url(r'^carrinho/([0-9]+)$', views.ProdutoDoCarrinhoDoCarrinhoApi),

    url(r'^imagem$', views.SaveFile),

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)