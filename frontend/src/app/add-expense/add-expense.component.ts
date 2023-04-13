import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ExpenseService } from '../services/expense.service';
import { Category } from '../category/category.model';
import { CategoryService } from '../services/category.service';

@Component({
  selector: 'app-add-expense',
  templateUrl: './add-expense.component.html',
  styleUrls: ['./add-expense.component.css']
})
export class AddExpenseComponent {
  categories: Category[];

  form: FormGroup;

  constructor(private expenseService: ExpenseService, private categoryService: CategoryService, private router: Router) {}

  ngOnInit(){
    this.fetchCategories();
    this.form = new FormGroup({
      'date': new FormControl(null, Validators.required),
      'note': new FormControl(''),
      'expense': new FormControl(0.00, [ Validators.required, Validators.min(0) ]),
      'category': new FormControl(null, Validators.required)
    });
  }

  private fetchCategories() {
    this.categoryService.getAllCategories().subscribe({
      next: res => {
        if (res['statusCode'] === 200) {
          this.categories = res['data'];
        }
      }
    })
  }

  onSubmit() {
    console.log(this.form.value);
    // save expense
    this.expenseService.addExpense(this.form.value);
    this.router.navigate(['/reports']);
  }
}
