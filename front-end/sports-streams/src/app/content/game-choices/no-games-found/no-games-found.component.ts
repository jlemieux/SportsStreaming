import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Sport } from 'src/app/shared/models/sport';
import { SportsService } from 'src/app/shared/services/sports.service';

@Component({
  selector: 'app-no-games-found',
  templateUrl: './no-games-found.component.html',
  styleUrls: ['./no-games-found.component.scss']
})
export class NoGamesFoundComponent implements OnInit {

  @Input() sport!: Sport;
  activeSport$: Observable<Sport>;

  constructor(private sportsService: SportsService) {
    this.activeSport$ = this.sportsService.activeSport$;
  }

  ngOnInit(): void {
  }

}
