import { Component, OnInit } from '@angular/core';
import { HttpService } from '../services/http.service';
import { Router } from '@angular/router';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-expense',
  templateUrl: './expense.component.html',
  styleUrls: ['./expense.component.css']
})
export class ExpenseComponent implements OnInit {

  expense: any = []
  categories: any = []
  openModal: Boolean = false;
  
  expenseForm = new FormGroup({
    ID: new FormControl(0),
    cat_id: new FormControl(0),
    amount: new FormControl(0, Validators.required),
    description: new FormControl(''),
    expense_date: new FormControl('', Validators.required)
  });

  constructor(private http: HttpService, private router: Router) {}

  ngOnInit(): void {

    // get expense data
    this.http.get('/expense/getAllForCurrentUser').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.expense = res['data']
        }
        else
          this.router.navigate(['/error'])
      }),
      (err => {
        this.router.navigate(['/error'])
      })
    );

    // get categories
    this.http.get('/category/getAllForCurrentUser').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.categories = res['data']
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
    let data = this.expenseForm.value;
    console.log(data)

    if(data["ID"] == null || data["ID"] == 0) {
      this.http.post('/expense/addExpense', data).subscribe(
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
      this.http.post('/expense/editExpense', data).subscribe(
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

    // load expense data
    this.http.get('/expense/getAllForCurrentUser').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.expense = res['data']
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
    this.expenseForm.reset();
  }

  edit(exp: any){
    this.expenseForm.reset();
    this.expenseForm = new FormGroup({
      ID: new FormControl(exp["ID"], Validators.required),
      cat_id: new FormControl(exp["CAT_ID"], Validators.required),
      amount: new FormControl(exp["AMOUNT"], Validators.required),
      description: new FormControl(exp["DESCRIPTION"]),
      expense_date: new FormControl(exp["EXPENSE_DATE"], Validators.required)
    });
  }

  delete(eid: number){
    console.log(eid)
    this.http.post('/expense/deleteExpense', {id: eid}).subscribe(
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

    // load expense data
    this.http.get('/expense/getAllForCurrentUser').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.expense = res['data']
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
