import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Conta } from 'src/app/models/conta';

import { SharedService } from 'src/app/service/shared.service';

@Component({
  selector: 'app-formlogin',
  templateUrl: './formlogin.component.html',
  styleUrls: ['./formlogin.component.css']
})
export class FormloginComponent implements OnInit {

  emailUsuario: string = "";
  senhaUsuario: string = "";
  usuario: Partial<Conta> = {
    ContaEmail: "",
    ContaSenha: ""
  }

  constructor(
    private router: Router,
    private service: SharedService
  ) { }

  //Primeiro método que é executado quando o componente é carregado
  ngOnInit(): void {
  }
  
  //Método para navegar para a página de cadastro
  Navegar(rota: string) {
    this.router.navigate(['/acesso' + rota]);
  }

  //Método para procurar com uma conta e logar com ela
  EntrarComConta() {

    this.usuario.ContaEmail = this.emailUsuario;
    this.usuario.ContaSenha = this.senhaUsuario;

    //Subscribe serve para garantir que uma resposta já foi recebida antes de continuar a execução, ou seja, define essa operação como assíncrona
    this.service.getContaPorUsuarioESenha(this.usuario).subscribe(data => {
      console.log(data);
      if (data.Code == 200){
        localStorage.setItem("currentUser", JSON.stringify(data.Objeto)); //Armazenar os dados do usuário logado no localStorage para acessar a qualquer momento
        this.router.navigate(['/home/lojas/']); //Navegar para a página inicial
      }
    });
  }
}
