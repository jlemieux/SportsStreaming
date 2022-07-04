import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-score-and-time',
  templateUrl: './score-and-time.component.html',
  styleUrls: ['./score-and-time.component.scss']
})
export class ScoreAndTimeComponent implements OnInit {

  @Input() score!: string;
  @Input() time!: string;
  
  constructor() { }

  ngOnInit(): void {
  }

}
