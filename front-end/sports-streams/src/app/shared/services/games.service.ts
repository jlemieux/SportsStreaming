import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, ReplaySubject } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Game } from '../models/game';
import { Sport } from '../models/sport';
import { SportsService } from './sports.service';

@Injectable({
  providedIn: 'root'
})
export class GamesService {

  games$ = new ReplaySubject<Observable<Game[]>>(1);
  private games: SportToGames = {} as SportToGames;

  constructor(
    private http: HttpClient,
    private sportsService: SportsService
  ) {
    this.sportsService.getSports().subscribe((sports: Sport[]) => {
      sports.forEach((sport: Sport) => {
        this.games[sport] = new ReplaySubject<Game[]>(1);
        this.fetchGames(sport);
      });
      this.sportsService.activeSport$.next(Sport.BASEBALL); // default to baseball
    });

    this.sportsService.activeSport$.subscribe((sport: Sport) => {
      this.games$.next(this.games[sport]);
    });
  }

  private fetchGames(sport: Sport): void {
    const supportedSports = [Sport.BASEBALL];
    if (!supportedSports.includes(sport)) {
      this.games[sport].next([]);
      return;
    }
    this.http.get<Game[]>(`${environment.API}/${sport}`).subscribe({
      next: (games: Game[]) => {
        const gamesInProgress = games.filter(game => game.time.toLowerCase().includes('inning'));
        const gamesNotInProgress = games.filter(game => !game.time.toLowerCase().includes('inning'));
        this.games[sport].next(gamesInProgress.concat(gamesNotInProgress));
      },
      error: (error: HttpErrorResponse) => {
        // usually only want to show "No Games Found" if its 404, but just do that so its not blank screen
        // if (error.status === 404) {
        //   this.games[sport].next([])
        // }
        // if 500 error, just show "No Games" instead of screen blank for now...
        this.games[sport].next([])
      }
    });
  }

}

type SportToGames =  { [sport in Sport]: ReplaySubject<Game[]> };
