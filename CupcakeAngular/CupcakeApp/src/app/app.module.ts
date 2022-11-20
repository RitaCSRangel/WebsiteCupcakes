//Import para componentes
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './componentes/home/home.component';
import { AcessoComponent } from './componentes/acesso/acesso.component';
import { LojasComponent } from './componentes/home/lojas/lojas.component';
import { CardapioComponent } from './componentes/home/cardapio/cardapio.component';
import { CarrinhoComponent } from './componentes/home/carrinho/carrinho.component';
import { FormloginComponent } from './componentes/acesso/formlogin/formlogin.component';
import { FormcadastroComponent } from './componentes/acesso/formcadastro/formcadastro.component';
import { HeaderComponent } from './componentes/header/header.component';
import { FooterComponent } from './componentes/footer/footer.component';
import { ProdutosdalojaComponent } from './componentes/home/produtosdaloja/produtosdaloja.component';

//Import para serviços
import { SharedService } from './service/shared.service';

//Imports adicionais
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AcessoComponent,
    LojasComponent,
    CardapioComponent,
    CarrinhoComponent,
    FormloginComponent,
    FormcadastroComponent,
    HeaderComponent,
    FooterComponent,
    ProdutosdalojaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
