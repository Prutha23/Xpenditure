import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {

  f1: Boolean = true;
  f2: Boolean = false;
  f3: Boolean = false;
  
  constructor(private auth:AuthService, private router: Router){ }

  ngOnInit(): void {
    
  }

  toggleColor(flag: string){
    if(flag === 'f1'){
      this.f1=true
      this.f2=false
      this.f3=false
    }
    else if(flag === 'f2'){
      this.f1=false
      this.f2=true
      this.f3=false
    }
    else if(flag === 'f3'){
      this.f1=false
      this.f2=false
      this.f3=true
    }
  }

  logout(){
    this.auth.deauthenticate()
    this.router.navigate(['/login'])
  }
}
