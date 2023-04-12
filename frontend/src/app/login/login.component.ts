import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  message = '';
  loginForm = new FormGroup({
    username: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required)
  });

  constructor(private auth: AuthService,
              private router: Router) { }

  ngOnInit() {
    if(this.auth.isAuthenticated()) {
      if(this.auth.isAdmin())
        this.router.navigate(['/admin']);
      else if(this.auth.isUser())
        this.router.navigate(['/home']);
      else
        this.router.navigate(['/error']);
    }
  }

  onSubmit() {
    let username = this.loginForm.get('username')?.value;
    const password = this.loginForm.get('password')?.value;
    console.log(`logging in: ${username}`);
    this.auth.authenticate(username, password).subscribe(
      (res) => {
        this.message = '';
        if(this.auth.isAdmin())
          this.router.navigate(['/admin']);
        else if(this.auth.isUser())
          this.router.navigate(['/home']);
        else
          this.router.navigate(['/error']);
      },
      (error) => {
        this.message = error;
      }
    );
  }
}
