import { Component, Input, OnInit } from '@angular/core';
import { Game } from 'src/app/shared/models/game';

@Component({
  selector: 'app-game-choice',
  templateUrl: './game-choice.component.html',
  styleUrls: ['./game-choice.component.scss']
})
export class GameChoiceComponent implements OnInit {

  @Input() game!: Game;

  constructor() { }

  ngOnInit(): void {
  }

}
