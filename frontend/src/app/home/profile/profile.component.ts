import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  message: string = ""
  profileForm = new FormGroup({
    uId: new FormControl(0, Validators.required),
    fName: new FormControl('', Validators.required),
    lName: new FormControl('', Validators.required),
    username: new FormControl('', Validators.required),
    phoneno: new FormControl(''),
    addressLine1: new FormControl('', Validators.required),
    street: new FormControl('', Validators.required),
    province: new FormControl('', Validators.required),
    zipCode: new FormControl('', Validators.required),
    country: new FormControl('', Validators.required)
  });

  constructor(private http: HttpService, private auth: AuthService, private router: Router) {}

  ngOnInit(): void {

    this.profileForm.reset();

    // get data
    this.http.get('/users/profile').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.profileForm = new FormGroup({
            uId: new FormControl(res['data']["U_ID"], Validators.required),
            fName: new FormControl(res['data']["FNAME"], Validators.required),
            lName: new FormControl(res['data']["LNAME"], Validators.required),
            username: new FormControl(res['data']["EMAILID"], Validators.required),
            phoneno: new FormControl(res['data']["PHONENO"]),
            addressLine1: new FormControl(res['data']["ADDRESSLINE1"], Validators.required),
            street: new FormControl(res['data']["STREET"], Validators.required),
            province: new FormControl(res['data']["PROVINCE"], Validators.required),
            zipCode: new FormControl(res['data']["ZIPCODE"], Validators.required),
            country: new FormControl(res['data']["COUNTRY"], Validators.required)
          });
        }
        else
          this.router.navigate(['/error'])
      }),
      (err => {
        this.router.navigate(['/error'])
      })
    );
  }

  onSubmit(){
    this.http.post('/users/profileUpdate', this.profileForm.value).subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this,this.message = res["message"]
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
