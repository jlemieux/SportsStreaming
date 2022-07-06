import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { GamesService } from 'src/app/shared/services/games.service';

@Component({
  selector: 'app-shutdown',
  templateUrl: './shutdown.component.html',
  styleUrls: ['./shutdown.component.css']
})
export class ShutdownComponent implements OnInit {

  buttonText = 'Shutdown';
  shutdownError = false;
  loading = false;
  shutdownComplete = false;

  constructor(private gamesService: GamesService) { }

  ngOnInit(): void {
  }

  shutdown(): void {
    this.loading = true;
    this.gamesService.shutdownServer().subscribe({
      error: (err: HttpErrorResponse) => {
        this.shutdownError = true;
        this.loading = false;
        this.buttonText = 'Error Shutting Down!';
      },
      complete: () => {
        this.loading = false;
        this.shutdownComplete = true;
        this.buttonText = 'Shutdown Complete';
      }
    });
  }

}
