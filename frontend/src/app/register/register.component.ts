import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';
import { HttpService } from '../services/http.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  message = '';
  registrationForm = new FormGroup({
    fName: new FormControl('', Validators.required),
    lName: new FormControl('', Validators.required),
    username: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required),
    phoneno: new FormControl(''),
    addressLine1: new FormControl('', Validators.required),
    street: new FormControl('', Validators.required),
    province: new FormControl('', Validators.required),
    zipCode: new FormControl('', Validators.required),
    country: new FormControl('', Validators.required)
  });

  constructor(private auth: AuthService, private router: Router, private http: HttpService) { }

  ngOnInit() {
  }

  onSubmit() {
    
    this.http.post('/auth/register', this.registrationForm.value).subscribe(
      (res) => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.router.navigate(['/login']);
        }
        else
          this.message = res["message"];
      },
      (error) => {
        this.message = 'Something went wrong!';
      }
    );
  }
}
