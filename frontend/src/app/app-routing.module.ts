import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { AuthGuard } from './services/auth.guard';
import { AdminGuard } from './services/admin.guard';
import { ErrorComponent } from './error/error.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { RegisterComponent } from './register/register.component';
import { UserDetailsComponent } from './user-details/user-details.component';
import { AddExpenseComponent } from './add-expense/add-expense.component';
import { ReportsComponent } from './reports/reports.component';
import { CategoryComponent } from './category/category.component';

const routes: Routes = [
  {
    path: '',
    component: LandingPageComponent
  },
  {
    path: 'register',
    component: RegisterComponent
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'logout',
    component: LogoutComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'u',
    component: HomeComponent,
    canActivate: [AuthGuard],
    canActivateChild: [AuthGuard],
    children: [
      { path: 'home', component: HomeComponent },
      // { path: 'admin-content', component: AdminContentComponent, canActivate: [AdminGuard] },
      { path: 'error', component: ErrorComponent }
    ]
  },
  {
    path: 'personal-details',
    component: UserDetailsComponent,
    canActivate: [ AuthGuard ]
  },
  {
    path: 'add-expense',
    component: AddExpenseComponent,
    canActivate: [ AuthGuard ]
  },
  {
    path: 'reports',
    component: ReportsComponent,
    canActivate: [ AuthGuard ]
  },
  {
    path: 'categories',
    component: CategoryComponent,
    canActivate: [ AuthGuard ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
