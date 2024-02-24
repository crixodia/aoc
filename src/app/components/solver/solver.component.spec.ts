import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SolverComponent } from './solver.component';

describe('SolverComponent', () => {
  let component: SolverComponent;
  let fixture: ComponentFixture<SolverComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SolverComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SolverComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
