import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UtilService {

  constructor(private http: HttpClient) { }

  shutdownServer(): Observable<{shutdown: boolean}> {
    return this.http.post<{shutdown: boolean}>(`${environment.API}/shutdown`, {});
  }
  
}
