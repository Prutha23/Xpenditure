import { Component, OnInit } from '@angular/core';
import { Expense, ExpenseService } from '../services/expense.service';

@Component({
  selector: 'app-reports',
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent implements OnInit {

  expenses: Expense[] = [];
  total: number = 0;

  constructor(private expenseService: ExpenseService) {

  }

  ngOnInit(): void {
    this.expenses = this.expenseService.getAllExpenses();
    this.total = this.expenses.reduce((total, curr) => {
      return total + curr.expense;
    }, 0);
  }
}
