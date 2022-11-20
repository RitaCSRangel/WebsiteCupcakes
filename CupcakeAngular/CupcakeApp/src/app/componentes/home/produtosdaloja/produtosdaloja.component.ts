import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { SharedService } from 'src/app/service/shared.service';

import { Conta } from 'src/app/models/conta';
import { Cardapio } from 'src/app/models/cardapio';
import { Produto } from 'src/app/models/produto';
import { ProdutoDoCarrinho } from 'src/app/models/produtodocarrinho';

@Component({
  selector: 'app-produtosdaloja',
  templateUrl: './produtosdaloja.component.html',
  styleUrls: ['./produtosdaloja.component.css']
})
export class ProdutosdalojaComponent implements OnInit {

  corBotaoAdicionar: string = "#AAB9AC";
  corBotaoDecrementar: string = "#AAB9AC";

  usuarioLogado: Conta = {
    ContaId: 0,
    ContaNome: "",
    ContaTipo: 0,
    ContaRua: "",
    ContaBairro: "",
    ContaNumero: "",
    ContaComplemento: "",
    ContaCep: "",
    ContaSenha: "",
    ContaEmail: "",
    ContaStatus: 0
  };

  idCardapio: Partial<Cardapio> = {
    CardapioUsuario: 0
  };
  idProduto: Partial<Produto> = {
    ProdutoId: 0
  };
  cardapios: Cardapio[] = [];
  produtos: Produto[] = [];
  produtosAdicionadosCarrinho: ProdutoDoCarrinho[] = [];


  constructor(
    private service: SharedService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.usuarioLogado = JSON.parse(localStorage.getItem("currentUser")!);
    this.ObterTodosProdutosDoCardapio();
  }

  ObterTodosProdutosDoCardapio() {

    this.idCardapio.CardapioUsuario = Number(localStorage.getItem("currentStore"));

    //Buscando um cardápio com o id da loja selecionada
    this.service.getCardapioDoUsuario(this.idCardapio).subscribe(menu => {

      //Inserindo o cardapio ou cardapios obtido(s) em um array de cardapios
      this.cardapios = menu.Objeto;

      /*
      Essa busca pode retornar um ou mais itens. Caso retorne somente um o resultado não será um array de cardápios, mas sim um objeto único. 
      Por conta dessa possibilidade se fez necessário garatir que o foreach funcionaria mesmo com objetos, logo o uso do Object.entries para gerar um array de key value foi 
      utilizado.
      */
      Object.entries(this.cardapios).forEach(([key, value]) => {

        //Quando o array bater em uma key de CardapioProduto
        if (key == 'CardapioProduto') {

          this.idProduto.ProdutoId = Number(value);

          //Faz a busca desse produto
          this.service.getProdutosDoCardapio(this.idProduto).subscribe((products) => {
            this.produtos = products.Objeto as [];
          })

        }

      });

    });

  }

  IncrementarProdutosDoCarrinho(produto: any) {

    /*
    A partir do produto que recebeu o clique, verificar se ele já foi adicionado ao produtosAdicionadosCarrinho.
    
    Se encontrar ele marca a tag de encontrouProduto como sim e, posteriormente, incrementa a quantidade da variável 
    que é mostrada no HTML, representando que mais uma unidade desse item foi adicionada.

    Se não encontrar então acrescenta esse item ao produtosAdicionadosCarrinho e define sua quantidade como 1.
    */

    const idProdutoClicado = produto.ProdutoId; //id do produto que recebeu o click
    let index = 0;
    let encontrouProduto = false;

    //Para cada produto adicionado ao carrinho
    this.produtosAdicionadosCarrinho.forEach(function (prod) {

      if (prod.ProdutoDoCarrinhoProduto == idProdutoClicado) { //Verificar se o id do produto dentro do carrinho é o mesmo id do produto que recebeu p clique
        encontrouProduto = true; //Se encontrou para aqui
      } else {
        if (encontrouProduto == false) {
          index++; //Se não encontrou continua procurando
        }
      }

    })

    //Se encontrou então incrementa a quantidade dele
    if (encontrouProduto) {
      if (this.produtosAdicionadosCarrinho[index].ProdutoDoCarrinhoQuantidade == produto.ProdutoQuantidade) { //Se bateu o valor máximo não incrementa
        this.corBotaoAdicionar = 'gray';
      }
      else { //Se não bateu o valor máximo ainda pode incrementar
        this.corBotaoAdicionar = "#AAB9AC";
        this.produtosAdicionadosCarrinho[index].ProdutoDoCarrinhoQuantidade++;
      }
    }

    //Se o produto nunca foi encontrado no array então adiciona ele
    if (encontrouProduto == false) {

      const novoProdutoDoCarrinho = {
        ProdutoDoCarrinhoId: 0,
        ProdutoDoCarrinhoNome: produto.ProdutoNome,
        ProdutoDoCarrinhoPreco: produto.ProdutoPreco,
        ProdutoDoCarrinhoQuantidade: produto.ProdutoQuantidade,
        ProdutoDoCarrinhoUsuario: this.usuarioLogado.ContaId,
        ProdutoDoCarrinhoProduto: produto.ProdutoId
      }

      this.produtosAdicionadosCarrinho.push(novoProdutoDoCarrinho);

    }

    //this.AtualizarTotalDeItens();

  }

  DecrementarProdutosDoCarrinho(produto: any) {
    const idProdutoClicado = produto.ProdutoId; //id do produto que recebeu o click
    let index = 0;
    let encontrouProduto = false;

    this.produtosAdicionadosCarrinho.forEach(function (prod) {

      if (prod.ProdutoDoCarrinhoProduto == idProdutoClicado) {
        encontrouProduto = true; //Se encontrou para aqui
      } else {
        if (encontrouProduto == false) {
          index++; //Se não encontrou continua procurando
        }
      }

    })

    //Se encontrou então decrementa a quantidade dele
    if (encontrouProduto) {
      if (this.produtosAdicionadosCarrinho[index].ProdutoDoCarrinhoQuantidade == 0) { //Se bateu o valor máximo não incrementa
        this.corBotaoAdicionar = 'gray';
      }
      else { //Se não bateu o valor mínimo ainda pode decrementar
        this.corBotaoAdicionar = "#AAB9AC";
        this.produtosAdicionadosCarrinho[index].ProdutoDoCarrinhoQuantidade++;
      }
    }

    //this.AtualizarTotalDeItens();
  }

}
