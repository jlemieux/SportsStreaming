import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-team-name',
  templateUrl: './team-name.component.html',
  styleUrls: ['./team-name.component.css']
})
export class TeamNameComponent implements OnInit {

  @Input() name!: string;
  
  constructor() { }

  ngOnInit(): void {
  }

}
