import { Injectable } from '@angular/core';

import { HttpClient, HttpParams } from '@angular/common/http'; //Usado para lidar com os requests
import { Observable } from 'rxjs'; //Usado para lidar com requests e responses assíncronos

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  //URL da API criada com o Django para utilizar os métodos da Cupcake API
  readonly CupcakeApiUrl = "http://127.0.0.1:8000/";
  readonly CupcakeApiimageUrl = this.CupcakeApiUrl + "media/" //Não está sendo usado nesse projeto no momento.

  constructor(
    private http: HttpClient
  ) { }

  /*
  Antes de começar é importante ressaltar que o uso do any se refere a um dado sem tipo. 
  É possível (e recomendável) substituir o any por um tipo definido no model, porém
  para fins de exemplificação deixarei como any aqui. 
  
  Exemplo usando any: Observable<any[]> e get<any[]>
  Exemplo usando o model de Conta: Observable<Conta[]> e get<Conta[]>

  */

  //--------------- Métodos relacionados a entidade de conta --------------- 

  //Obter todas as contas
  getListaConta(): Observable<any> {
    return this.http.get<Response>(this.CupcakeApiUrl + "conta/");
  }

  //Criar uma conta
  addConta(conta: any) {
    return this.http.post(this.CupcakeApiUrl + "conta/", conta);
  }

  //Atualizar uma conta
  updateConta(conta: any) {
    return this.http.put(this.CupcakeApiUrl + "conta/", conta);
  }

  //Deletar uma conta
  deleteConta(contaId: any) {
    return this.http.delete(this.CupcakeApiUrl + "conta/", contaId);
  }

  //Obter uma conta específica usando o id
  getContaPorId(conta: any) {
    return this.http.get(this.CupcakeApiUrl + "conta/", conta);
  }

  getContaPorUsuarioESenha(usuarioESenha: any): Observable<any> {
    return this.http.post<Response>(this.CupcakeApiUrl + "auth/", usuarioESenha);
  }

  //--------------- Métodos relacionados a entidade de Cardapio (Produtos do Cardapio) --------------- 

  //Obter todos os cardapios
  getListaCardapio(): Observable<any> {
    return this.http.get<Response>(this.CupcakeApiUrl + "cardapio/");
  }

  //Criar um cardapio
  addCardapio(conta: any) {
    return this.http.post(this.CupcakeApiUrl + "cardapio/", conta);
  }

  //Atualizar um cardapio
  updateCardapio(conta: any) {
    return this.http.put(this.CupcakeApiUrl + "cardapio/", conta);
  }

  //Deletar um cardapio
  deleteCardapio(contaId: any) {
    return this.http.delete(this.CupcakeApiUrl + "cardapio/", contaId);
  }

  //Obter produtos do cardápio de um usuário
  getCardapioDoUsuario(ContaId: any): Observable<any> {
    return this.http.post<Response>(this.CupcakeApiUrl + "cardapioUsuario/", ContaId);
  }

  //Obter produtos do cardápio de um usuário
  getProdutosDoCardapio(CardapioProduto: any): Observable<any> {
    return this.http.post<Response>(this.CupcakeApiUrl + "produtosCardapio/", CardapioProduto);
  }

  //--------------- Métodos relacionados a entidade de Produto --------------- 

  //Obter todos os produtos
  getListaProduto(): Observable<any> {
    return this.http.get<Response>(this.CupcakeApiUrl + "produto/");
  }

  //Criar um produto
  addProduto(conta: any) {
    return this.http.post(this.CupcakeApiUrl + "produto/", conta);
  }

  //Atualizar um produto
  updateProduto(conta: any) {
    return this.http.put(this.CupcakeApiUrl + "produto/", conta);
  }

  //Deletar um produto
  deleteProduto(contaId: any) {
    return this.http.delete(this.CupcakeApiUrl + "produto/", contaId);
  }

  //--------------- Métodos relacionados a entidade de Produto do Carrinho --------------- 

  //Obter todos os produtos do carrinho
  getListaProdutosDoCarrinho(): Observable<any> {
    return this.http.get<Response>(this.CupcakeApiUrl + "carrinho/");
  }

  //Criar um produto do carrinho
  addProdutoDoCarrinho(conta: any) {
    return this.http.post(this.CupcakeApiUrl + "carrinho/", conta);
  }

  //Atualizar um produto do carrinho
  updateProdutoDoCarrinho(conta: any) {
    return this.http.put(this.CupcakeApiUrl + "carrinho/", conta);
  }

  //Deletar um produto do carrinho
  deleteProdutoDoCarrinho(contaId: any) {
    return this.http.delete(this.CupcakeApiUrl + "carrinho/", contaId);
  }

  //Obter produtos do carrinho do carrinho de um usuário específico
  getProdutoDoCarrinhoPorUsuario(idDaConta: string): Observable<any[]> {
    let parametro = new HttpParams().set('ProdutoDoCarrinhoUsuario', idDaConta);
    return this.http.get<Response[]>(this.CupcakeApiUrl + "carrinho/", { params: parametro });
  }

}
