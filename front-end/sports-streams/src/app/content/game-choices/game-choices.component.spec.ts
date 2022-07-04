import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GameChoicesComponent } from './game-choices.component';

describe('GameChoicesComponent', () => {
  let component: GameChoicesComponent;
  let fixture: ComponentFixture<GameChoicesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GameChoicesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GameChoicesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
