import { Component, OnInit } from '@angular/core';
import { HttpService } from '../services/http.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{

  constructor(private http: HttpService) {}

  ngOnInit(){
    // example
    let catdId = 2;
    this.http.get('/expense/getByCategoryId?cat_id='+catdId).subscribe(res=>{
      console.log(res)
    })
  }
}