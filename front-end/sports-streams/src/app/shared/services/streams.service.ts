import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { EMPTY, Observable, ReplaySubject } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { Sport } from '../models/sport';
import { GameStream, GameStreamError } from '../models/stream';

@Injectable({
  providedIn: 'root'
})
export class StreamsService {

  // infinite buffer, so swapping sports will remember which streams have errored
  gameStreamError$ = new ReplaySubject<GameStreamError>();

  constructor(private http: HttpClient) { }

  watchStream(id: string, sport: Sport): Observable<GameStream> {
    return this.http.get<GameStream>(`${environment.API}/${sport}/${id}`).pipe(
      tap((stream: GameStream) => {
        window.open(stream.link, '_blank');
      }),
      catchError((error: HttpErrorResponse) => {
        const message = { gameId: id, reason: 'Error!' };
        if (error.status === 404) {
          if (error.error.name === 'NoWeakSpellFound') {
            message.reason = 'No Weak_Spell';
          }
          else if (error.error.name === 'NoStreamersFound') {
            message.reason = 'No Streamers';
          }
          else if (error.error.name === 'NoGameIdFound') {
            message.reason = 'No Game ID';
          }
        }
        this.gameStreamError$.next(message);
        return EMPTY;
      })
    );
  }

}
