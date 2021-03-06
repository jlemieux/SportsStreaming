import { Component, Input, OnInit } from '@angular/core';
import { filter, take } from 'rxjs/operators';
import { BaseballGame, Game } from 'src/app/shared/models/game';
import { GameStreamError } from 'src/app/shared/models/stream';
import { GamesService } from 'src/app/shared/services/games.service';
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

  constructor(private streamsService: StreamsService) { }

  watchStream(): void {
    this.loading = true;
    this.streamsService.watchStream((this.game as BaseballGame).id).subscribe({
      complete: () => {
        this.loading = false;
      }
    });
  }

  ngOnInit(): void {
    this.streamsService.gameStreamError$.pipe(
      filter((err: GameStreamError) => err.gameId === (this.game as BaseballGame).id),
      take(1)
    ).subscribe({
      next: (err: GameStreamError) => {
        this.buttonText = err.reason;
        this.streamError = true;
      }
    });
  }

}
