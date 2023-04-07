import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ExpenseService } from '../services/expense.service';

@Component({
  selector: 'app-add-expense',
  templateUrl: './add-expense.component.html',
  styleUrls: ['./add-expense.component.css']
})
export class AddExpenseComponent {
  categories = ['food', 'houseware', 'clothes', 'electric bill', 'transportation', 'contact fee', 'houseing expense', 'tim', 'personal', 'grocery', 'indian store'];

  form: FormGroup;

  constructor(private expenseService: ExpenseService, private router: Router) {}

  ngOnInit(){
    this.form = new FormGroup({
      'date': new FormControl(null, Validators.required),
      'note': new FormControl(''),
      'expense': new FormControl(0.00, [ Validators.required, Validators.min(0) ]),
      'category': new FormControl(null, Validators.required)
    });
  }

  onSubmit() {
    console.log(this.form.value);
    // save expense
    this.expenseService.addExpense(this.form.value);
    this.router.navigate(['/reports']);
  }
}
