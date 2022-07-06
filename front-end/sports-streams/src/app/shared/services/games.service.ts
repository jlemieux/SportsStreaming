import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, EMPTY, Observable, ReplaySubject, tap } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Game } from '../models/game';
import { Sport } from '../models/sport';
import { GameStream, GameStreamError } from '../models/stream';
import { SportsService } from './sports.service';

@Injectable({
  providedIn: 'root'
})
export class GamesService {

  games$ = new ReplaySubject<Observable<Game[]>>(1);
  private games: SportToGames = {} as SportToGames;

  // infinite buffer, so swapping sports will remember which streams have errored
  gameStreamError$ = new ReplaySubject<GameStreamError>();

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
    this.http.get<Game[]>(`${environment.HOST}/${sport}`).subscribe({
      next: (games: Game[]) => {
        this.games[sport].next(games);
      },
      error: (error: HttpErrorResponse) => {
        if (error.status === 404) {
          this.games[sport].next([])
        }
        // if 500 error, just leave screen blank for now...
      }
    });
  }

  watchStream(id: string): Observable<GameStream> {
    return this.http.get<GameStream>(`${environment.HOST}/baseball/${id}`).pipe(
      tap((stream: GameStream) => window.open(stream.link, '_blank')),
      catchError((error: HttpErrorResponse) => {
        const message = { gameId: id, reason: 'Error!' };
        if (error.status === 404) {
          if (error.error.name === 'NoWeakSpellFound') {
            message.reason = 'No Weak_Spell';
          }
          else if (error.error.name === 'NoStreamersFound') {
            message.reason = 'No Streamers';
          }
        }
        this.gameStreamError$.next(message);
        return EMPTY;
      })
    );
  }

  shutdownServer(): Observable<{shutdown: boolean}> {
    return this.http.post<{shutdown: boolean}>(`${environment.HOST}/shutdown`, {});
  }

}

type SportToGames =  { [sport in Sport]: ReplaySubject<Game[]> };
