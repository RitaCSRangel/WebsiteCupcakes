import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AcessoComponent } from './componentes/acesso/acesso.component';
import { FormcadastroComponent } from './componentes/acesso/formcadastro/formcadastro.component';
import { FormloginComponent } from './componentes/acesso/formlogin/formlogin.component';
import { CardapioComponent } from './componentes/home/cardapio/cardapio.component';
import { HomeComponent } from './componentes/home/home.component';
import { LojasComponent } from './componentes/home/lojas/lojas.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'acesso/login',
    pathMatch: 'full'
  },
  {
    path:'acesso',
    component: AcessoComponent,
    children: [
      {
        path: 'login',
        component: FormloginComponent
      },
      {
        path:'cadastro',
        component: FormcadastroComponent
      }
    ]
  },
  {
    path:'home',
    component: HomeComponent,
    children: [
      {
        path: 'lojas',
        component: LojasComponent
      },
      {
        path:'cardapio',
        component: CardapioComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
