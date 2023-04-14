import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-user-dashboard',
  templateUrl: './user-dashboard.component.html',
  styleUrls: ['./user-dashboard.component.css']
})
export class UserDashboardComponent implements OnInit {

  data: any = []

  constructor(private http: HttpService, private router: Router) {}

  ngOnInit(): void {

    // get dashboard data
    this.http.get('/user/dashboard').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.data = res['data']
          console.log(this.data)
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
