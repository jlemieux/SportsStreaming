import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SportChoiceComponent } from './sport-choice.component';

describe('SportChoiceComponent', () => {
  let component: SportChoiceComponent;
  let fixture: ComponentFixture<SportChoiceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SportChoiceComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SportChoiceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
