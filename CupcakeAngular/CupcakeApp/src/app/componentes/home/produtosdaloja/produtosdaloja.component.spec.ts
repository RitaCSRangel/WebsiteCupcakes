import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProdutosdalojaComponent } from './produtosdaloja.component';

describe('ProdutosdalojaComponent', () => {
  let component: ProdutosdalojaComponent;
  let fixture: ComponentFixture<ProdutosdalojaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProdutosdalojaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProdutosdalojaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
