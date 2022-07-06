import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BaseballStreamComponent } from './baseball-stream.component';

describe('BaseballStreamComponent', () => {
  let component: BaseballStreamComponent;
  let fixture: ComponentFixture<BaseballStreamComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BaseballStreamComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BaseballStreamComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
