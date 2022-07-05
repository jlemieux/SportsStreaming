import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Sport } from 'src/app/shared/models/sport';
import { SportsService } from 'src/app/shared/services/sports.service';

@Component({
  selector: 'app-sport-choice',
  templateUrl: './sport-choice.component.html',
  styleUrls: ['./sport-choice.component.scss']
})
export class SportChoiceComponent implements OnInit {

  @Input() sport!: Sport;
  activeSport$: Observable<Sport>;

  constructor(private sportsService: SportsService) {
    this.activeSport$ = this.sportsService.activeSport$;
  }

  chooseSport(): void {
    this.sportsService.activeSport$.next(this.sport);
  }

  ngOnInit(): void {
  }

}
