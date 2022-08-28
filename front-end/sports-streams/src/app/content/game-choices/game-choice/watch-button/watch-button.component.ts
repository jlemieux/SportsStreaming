import { Component, Input, OnInit } from '@angular/core';
import { filter, map, switchMap, take } from 'rxjs/operators';
import { BaseballGame, FootballGame, Game } from 'src/app/shared/models/game';
import { Sport } from 'src/app/shared/models/sport';
import { GameStreamError } from 'src/app/shared/models/stream';
import { SportsService } from 'src/app/shared/services/sports.service';
import { StreamsService } from 'src/app/shared/services/streams.service';

@Component({
  selector: 'app-watch-button',
  templateUrl: './watch-button.component.html',
  styleUrls: ['./watch-button.component.css']
})
export class WatchButtonComponent implements OnInit {

  @Input() game!: Game;

  buttonText = 'Watch';
  streamError = false;
  loading = false;

  constructor(private streamsService: StreamsService, private sportsService: SportsService) { }

  watchStream(): void {
    this.loading = true;
    this.sportsService.activeSport$.pipe(
      take(1),
      map(sport => {
        if (sport === Sport.BASEBALL) {
          return { id: (this.game as BaseballGame).id, sport };
        }
        if (sport === Sport.FOOTBALL) {
          return { id: btoa(this.game.link), sport };
        }
        // shouldnt get here since we have allowed sports, but to make typescript happy
        return { id: 'noIdFound', sport: Sport.BASEBALL };
      }),
      switchMap(({id, sport}) => this.streamsService.watchStream(id, sport))
    ).subscribe({
      complete: () => {
        this.loading = false;
      }
    });
  }

  ngOnInit(): void {
    this.streamsService.gameStreamError$.pipe(
      filter((err: GameStreamError) => (
        err.gameId === (this.game as BaseballGame).id ||
        err.gameId === btoa(this.game.link)
      )),
      take(1)
    ).subscribe({
      next: (err: GameStreamError) => {
        this.buttonText = err.reason;
        this.streamError = true;
      }
    });
  }

}
