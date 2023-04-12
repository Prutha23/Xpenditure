import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-reminders',
  templateUrl: './reminders.component.html',
  styleUrls: ['./reminders.component.css']
})
export class RemindersComponent implements OnInit {

  reminders: any = []
  openModal: Boolean = false

  reminderForm = new FormGroup({
    ID: new FormControl(0),
    EMAIL: new FormControl('', Validators.required),
    DESCRIPTION: new FormControl(''),
    DUE_DATE: new FormControl('', Validators.required)
  });

  constructor(private http: HttpService, private router: Router) {}

  ngOnInit(): void {

    // get data
    this.http.get('/reminder/getAllForCurrentUser').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.reminders = res['data']
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
    let data = this.reminderForm.value;
    console.log(data)

    if(data["ID"] == null || data["ID"] == 0) {
      this.http.post('/reminder/addReminder', data).subscribe(
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
    }
    else {
      this.http.post('/reminder/editReminder', data).subscribe(
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
    }

    // load data
    this.http.get('/reminder/getAllForCurrentUser').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.reminders = res['data']
        }
        else
          this.router.navigate(['/error'])
      }),
      (err => {
        this.router.navigate(['/error'])
      })
    );
  }

  clean(){
    this.reminderForm.reset();
  }

  edit(rem: any){
    this.reminderForm.reset();
    this.reminderForm = new FormGroup({
      ID: new FormControl(rem['ID']),
      EMAIL: new FormControl(rem['EMAIL'], Validators.required),
      DESCRIPTION: new FormControl(rem['DESCRIPTION']),
      DUE_DATE: new FormControl(rem['DUE_DATE'], Validators.required)
    });
  }

  delete(rid: number){
    console.log(rid)
    this.http.post('/reminder/deleteReminder', {ID: rid}).subscribe(
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

    // load data
    this.http.get('/reminder/getAllForCurrentUser').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.reminders = res['data']
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
