import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { AuthGuard } from './services/auth.guard';
import { AdminGuard } from './services/admin.guard';
import { ErrorComponent } from './error/error.component';
import { UserDetailsComponent } from './user-details/user-details.component';
import { AddExpenseComponent } from './add-expense/add-expense.component';
import { ReportsComponent } from './reports/reports.component';

const routes: Routes = [
  {
    path: 'login',
    component: LoginComponent
  },
  { path: 'home', component: HomeComponent },
  { path: 'personal-details', component: UserDetailsComponent },
  { path: 'add-expense', component: AddExpenseComponent },
  { path: 'reports', component: ReportsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
