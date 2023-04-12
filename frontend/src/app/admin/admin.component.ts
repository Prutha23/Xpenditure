import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {

  f1: Boolean = true;
  f2: Boolean = false;
  f3: Boolean = false;
  
  constructor(){ }

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
}
