import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  appServer = 'http://localhost:5000/api'

  constructor(private http: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };

  get(url: string): Observable<any> {
    // append query params in the url it self
    return this.http.get(this.appServer + url, this.httpOptions)
  }

  post(url: string, data: any): Observable<any> {
    return this.http.post(this.appServer + url, data, this.httpOptions)
  }
}
