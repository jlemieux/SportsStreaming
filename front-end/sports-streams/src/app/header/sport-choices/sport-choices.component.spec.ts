import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SportChoicesComponent } from './sport-choices.component';

describe('SportChoicesComponent', () => {
  let component: SportChoicesComponent;
  let fixture: ComponentFixture<SportChoicesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SportChoicesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SportChoicesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
