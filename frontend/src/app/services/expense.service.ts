import { Injectable } from '@angular/core';

export interface Expense {
  expense: number;
  category: string;
  date: Date;
  note: string;
}

@Injectable({
  providedIn: 'root'
})
export class ExpenseService {

  private expenses: Expense[] = [];

  constructor() {

  }

  addExpense(expense: Expense) {
    this.expenses.push(expense);
  }

  getAllExpenses(): Expense[] {
    return this.expenses.slice();
  }
}
