import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.css']
})
export class PaymentComponent {

  openModal: Boolean = false;
  endDate: any = ''
  amt: any = 0

  paymentForm = new FormGroup({
    PAYMENT_METHOD: new FormControl(0, Validators.required),
    CARD_HOLDER_NAME: new FormControl('', Validators.required),
    CARD_NO: new FormControl('', Validators.required),
  });

  constructor(private http: HttpService, private router: Router){
    let today = new Date();
    today.setMonth(today.getMonth() + 1);
    this.endDate = today.toISOString().slice(0,10);

    this.amt = 29
  }

  onSubmit(){
    let data = this.paymentForm.value;
    console.log(data)

    this.http.post('/subscription/payment', data).subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          alert(res["message"]);
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
    this.paymentForm.reset();
  }
}
