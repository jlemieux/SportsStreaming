import { Component, Input, OnInit } from '@angular/core';
import { BaseballGame, Game } from 'src/app/shared/models/game';
import { GamesService } from 'src/app/shared/services/games.service';

@Component({
  selector: 'app-watch-button',
  templateUrl: './watch-button.component.html',
  styleUrls: ['./watch-button.component.scss']
})
export class WatchButtonComponent implements OnInit {

  @Input() game!: Game;

  constructor(private gamesService: GamesService) { }

  watchStream(): void {
    this.gamesService.watchStream((this.game as BaseballGame).id);
  }

  ngOnInit(): void {
  }

}
