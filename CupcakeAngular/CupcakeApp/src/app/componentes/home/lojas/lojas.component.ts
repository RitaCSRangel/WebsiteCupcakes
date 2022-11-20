import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Conta } from 'src/app/models/conta';
import { SharedService } from 'src/app/service/shared.service';

@Component({
  selector: 'app-lojas',
  templateUrl: './lojas.component.html',
  styleUrls: ['./lojas.component.css']
})
export class LojasComponent implements OnInit {

  lojas: Conta[] = [];

  corAberto: string = "#AAB9AC";
  corFechado: string = "#a0545e";

  constructor(
    private router: Router,
    private service: SharedService
  ) { }

  ngOnInit(): void {

    //Obter todas as contas assim que o componente iniciar
    this.ObterTodasAsContas();

  }

  Navegar (rota: string, id: number) {
    localStorage.setItem("currentStore", String(id)); //Armazenar os dados da loja selecionada para usar no componente de carrinho
    this.router.navigate(['/home' + rota]);
  }

  ObterTodasAsContas () {
    this.service.getListaConta().subscribe(data => {
      console.log(data);
      this.lojas = data.Objeto; //Armazenar as lojas obtidas na variável de array
    });
  }

}
