import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ScoreAndTimeComponent } from './score-and-time.component';

describe('ScoreAndTimeComponent', () => {
  let component: ScoreAndTimeComponent;
  let fixture: ComponentFixture<ScoreAndTimeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ScoreAndTimeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ScoreAndTimeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
