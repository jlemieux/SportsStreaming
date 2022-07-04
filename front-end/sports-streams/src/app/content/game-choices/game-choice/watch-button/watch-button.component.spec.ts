import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WatchButtonComponent } from './watch-button.component';

describe('WatchButtonComponent', () => {
  let component: WatchButtonComponent;
  let fixture: ComponentFixture<WatchButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WatchButtonComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WatchButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
