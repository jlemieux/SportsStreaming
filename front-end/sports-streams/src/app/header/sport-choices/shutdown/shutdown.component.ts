import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { UtilService } from 'src/app/shared/services/util.service';

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

  constructor(private utilService: UtilService) { }

  ngOnInit(): void {
  }

  shutdown(): void {
    this.loading = true;
    this.utilService.shutdownServer().subscribe({
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
