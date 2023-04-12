import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-admin-dashboard',
  templateUrl: './admin-dashboard.component.html',
  styleUrls: ['./admin-dashboard.component.css']
})
export class AdminDashboardComponent implements OnInit {

  users = 0;
  premium_users = 0;
  expenses = 0;

  constructor(private http: HttpService, private router: Router) {}

  ngOnInit(){
    // load counts
    this.http.get('/admin/count').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.users = res['data']['USERS']
          this.premium_users = res['data']['PREMIUM_USERS']
          this.expenses = res['data']['EXPENSE']
        }
        else
          this.router.navigate(['/error'])
      }),
      (err => {
        this.router.navigate(['/error'])
      })
    );
  }
}
