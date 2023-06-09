import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { HttpService } from '../../services/http.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  users: any = []
  openModal: Boolean = false;
  pay_info:any = {
    ID: '',
    PAYMENT_DETAILS: {
      SUBSRIPTION_DATE: '',
      END_DATE: '',
      AMOUNT: ''
    }
  }
  constructor(private http: HttpService, private router: Router) {}

  ngOnInit(): void {

    // get user data
    this.http.get('/admin/getAllUsers').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.users = res['data']
        }
        else
          this.router.navigate(['/error'])
      }),
      (err => {
        this.router.navigate(['/error'])
      })
    );
  }

  changeActiveStatus(user: any){
    let active: number = 0;
    if(user.IS_ACTIVE == 1)
      active = 0
    else
      active = 1
    
    this.http.post('/admin/updateUserActiveStatus', {ID: user.ID, IS_ACTIVE: active}).subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
        }
        else
          this.router.navigate(['/error'])
      }),
      (err => {
        this.router.navigate(['/error'])
      })
    );

    // get user data
    this.http.get('/admin/getAllUsers').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.users = res['data']
        }
        else
          this.router.navigate(['/error'])
      }),
      (err => {
        this.router.navigate(['/error'])
      })
    );
  }

  approvePayment(info: any){
    console.log(info)
    this.http.post('/subscription/approve', {user_id: info.ID, start_date: info.PAYMENT_DETAILS.SUBSRIPTION_DATE, end_date: info.PAYMENT_DETAILS.END_DATE}).subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
        }
        else
          this.router.navigate(['/error'])
      }),
      (err => {
        this.router.navigate(['/error'])
      })
    );

    // get user data
    this.http.get('/admin/getAllUsers').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.users = res['data']
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
