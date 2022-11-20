import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Conta } from 'src/app/models/conta';

import { SharedService } from 'src/app/service/shared.service';

@Component({
  selector: 'app-formcadastro',
  templateUrl: './formcadastro.component.html',
  styleUrls: ['./formcadastro.component.css']
})
export class FormcadastroComponent implements OnInit {

  nomeUsuario: string = "";
  emailUsuario: string = "";
  senhaUsuario: string = "";

  novaConta: Partial<Conta> = { //Partial é usado aqui porque o campo ContaId não deve estar incluso
    ContaNome: "",
    ContaTipo: 1, //Tipo de Conta Padrão: Comum
    ContaRua: "",
    ContaBairro: "",
    ContaNumero: "",
    ContaComplemento: "",
    ContaCep: "",
    ContaSenha: "",
    ContaEmail: "",
    ContaStatus: 1 //Status Padrão: Ativo
  }

  constructor(
    private router: Router,
    private service: SharedService
  ) { }

  //Primeiro método que é executado quando o componente é carregado
  ngOnInit(): void {
  }

  Navegar (rota: string) {
    this.router.navigate(['/acesso' + rota]);
  }

  //Método para criar uma conta
  CadastrarConta (){

    //Preencher os dados da conta com os inputs do usuário
    this.novaConta.ContaNome = this.nomeUsuario;
    this.novaConta.ContaEmail = this.emailUsuario;
    this.novaConta.ContaSenha = this.senhaUsuario;

    //Subscribe serve para garantir que uma resposta já foi recebida antes de continuar a execução, ou seja, define essa operação como assíncrona
    this.service.addConta(this.novaConta).subscribe(data => {
      
      alert(data);

    });
  }
}
