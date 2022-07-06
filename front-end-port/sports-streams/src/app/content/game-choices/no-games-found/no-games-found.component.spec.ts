import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NoGamesFoundComponent } from './no-games-found.component';

describe('NoGamesFoundComponent', () => {
  let component: NoGamesFoundComponent;
  let fixture: ComponentFixture<NoGamesFoundComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NoGamesFoundComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NoGamesFoundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
