import { Injectable } from '@angular/core';
import { Observable, of, ReplaySubject } from 'rxjs';
import { Sport } from '../models/sport';

@Injectable({
  providedIn: 'root'
})
export class SportsService {

  activeSport$ = new ReplaySubject<Sport>(1);
  private sports = [Sport.BASEBALL, Sport.BASKETBALL, Sport.FOOTBALL, Sport.HOCKEY];

  constructor() { }

  getSports(): Observable<Sport[]> {
    return of(this.sports);
  }
}
