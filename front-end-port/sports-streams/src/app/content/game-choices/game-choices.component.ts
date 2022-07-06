import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { Game } from 'src/app/shared/models/game';
import { Sport } from 'src/app/shared/models/sport';
import { GamesService } from 'src/app/shared/services/games.service';
import { SportsService } from 'src/app/shared/services/sports.service';

@Component({
  selector: 'app-game-choices',
  templateUrl: './game-choices.component.html',
  styleUrls: ['./game-choices.component.css']
})
export class GameChoicesComponent implements OnInit {

  games$: Observable<Game[]>;

  constructor(
    private gamesService: GamesService
  ) {
    this.games$ = this.gamesService.games$.pipe(
      switchMap((games$: Observable<Game[]>) => games$)
    );
  }

  ngOnInit(): void {
  }

}
