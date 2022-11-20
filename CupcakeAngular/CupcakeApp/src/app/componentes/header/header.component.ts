import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Conta } from 'src/app/models/conta';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

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

  constructor(
    private router: Router
  ) { }

  ngOnInit(): void {
        //Obter o usuário que foi armazenado no local storage durante o login
        this.usuarioLogado = JSON.parse(localStorage.getItem("currentUser")!); //A exclamação serve como um --> if null then '' <-- para caso a string venha vazia
        console.log(this.usuarioLogado);
  }

  SairDaConta(){
    localStorage.removeItem("currentUser"); //Remover os dados do usuário logado no localStorage
    this.router.navigate(['/acesso/login']); //Navegar para a página de login
  }

}
