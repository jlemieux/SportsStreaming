import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Sport } from 'src/app/shared/models/sport';
import { SportsService } from 'src/app/shared/services/sports.service';

@Component({
  selector: 'app-sport-choices',
  templateUrl: './sport-choices.component.html',
  styleUrls: ['./sport-choices.component.css']
})
export class SportChoicesComponent implements OnInit {

  sports$: Observable<Sport[]>;

  constructor(private sportsService: SportsService) {
    this.sports$ = this.sportsService.getSports();
  }

  ngOnInit(): void {
  }

}
