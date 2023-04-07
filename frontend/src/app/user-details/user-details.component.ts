import { Component, OnInit } from '@angular/core';
import { Validators } from '@angular/forms';
import { FormControl } from '@angular/forms';
import { FormGroup } from '@angular/forms';

@Component({
  selector: 'app-user-details',
  templateUrl: './user-details.component.html',
  styleUrls: ['./user-details.component.css']
})
export class UserDetailsComponent implements OnInit {
  form: FormGroup;

  ngOnInit(): void {
    this.form = new FormGroup({
      'fname': new FormControl('', Validators.required),
      'lname': new FormControl('', Validators.required),
      'email': new FormControl('', [ Validators.required, Validators.email ]),
      'phone': new FormControl(null, Validators.required),
      'address': new FormControl(''),
      'street': new FormControl(''),
      'province': new FormControl(''),
      'zipcode': new FormControl(''),
      'country': new FormControl('')
    });
  }

  onSubmit() {
    
  }
}
