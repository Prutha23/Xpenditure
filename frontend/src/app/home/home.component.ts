import { Component, OnInit } from '@angular/core';
import { HttpService } from '../services/http.service';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{

  f1: Boolean = true;
  f2: Boolean = false;
  f3: Boolean = false;
  f4: Boolean = false;
  f5: Boolean = false;

  showDropdown: Boolean = false;

  constructor(private http: HttpService, public auth:AuthService) {}

  ngOnInit(){
    
  }

  toggleColor(flag: string){
    if(flag === 'f1'){
      this.f1=true
      this.f2=false
      this.f3=false
      this.f4=false
      this.f5=false
    }
    else if(flag === 'f2'){
      this.f1=false
      this.f2=true
      this.f3=false
      this.f4=false
      this.f5=false
    }
    else if(flag === 'f3'){
      this.f1=false
      this.f2=false
      this.f3=true
      this.f4=false
      this.f5=false
    }
    else if(flag === 'f4'){
      this.f1=false
      this.f2=false
      this.f3=false
      this.f4=true
      this.f5=false
    }
    else if(flag === 'f5'){
      this.f1=false
      this.f2=false
      this.f3=false
      this.f4=false
      this.f5=true
    }
  }
}
