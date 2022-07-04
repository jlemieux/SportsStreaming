import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, ReplaySubject } from 'rxjs';
import { Game } from '../models/game';
import { Sport } from '../models/sport';
import { SportsService } from './sports.service';

@Injectable({
  providedIn: 'root'
})
export class GamesService {

  mockGames: Game[] = [
    {
      team1: 'BuccsBuccsBuccsBuccsBuccs',
      team2: 'PatsBuccsBuccsBuccsBuccs',
      score: '4-18',
      time: '18:00',
      link: 'link-to-stream'
    },
    {
      team1: 'Falcons',
      team2: 'Tigers',
      score: '3-22',
      time: '7:20',
      link: 'link-to-stream'
    },
    {
      team1: 'GiantsGiantsGiantsGiantsGiants',
      team2: 'JetsJetsJetsJets',
      score: '0-0',
      time: '3RD INNING',
      link: 'link-to-stream'
    },
    {
      team1: 'Stealers',
      team2: 'Vikings',
      score: '34-14',
      time: 'STARTED',
      link: 'link-to-stream'
    },
  ];

  otherMockGames: Game[] = [
    {
      team1: 'Panthers',
      team2: 'Panthers',
      score: '2-50',
      time: '23:00',
      link: 'link-to-stream'
    },
    {
      team1: 'Chiefs',
      team2: 'Chiefs',
      score: '19-4',
      time: '9:30',
      link: 'link-to-stream'
    },
    {
      team1: 'Dolphins',
      team2: 'Dolphins',
      score: '3-3',
      time: '5th BOTTOM',
      link: 'link-to-stream'
    },
    {
      team1: 'Home',
      team2: 'Away',
      score: '20-20',
      time: 'PLAYING',
      link: 'link-to-stream'
    },
  ];

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
    if (sport === Sport.BASEBALL) {
      this.http.get<Game[]>(`http://localhost:5000/${sport}`).subscribe((games: Game[]) => {
        this.games[sport].next(games);
      });
    }
    else {
      this.games[sport].next([Sport.BASEBALL, Sport.FOOTBALL].includes(sport) ? this.mockGames : this.otherMockGames);
    }
  }

  watchStream(id: string): void {
    this.http.get<{link: string}>(`http://localhost:5000/baseball/${id}`).subscribe(resp => {
      window.open(resp.link, '_blank');
    });
  }

}

type SportToGames =  { [sport in Sport]: ReplaySubject<Game[]> };
