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
import { ExpenseComponent } from './home/expense/expense.component';
import { AdminComponent } from './admin/admin.component';
import { UserComponent } from './admin/user/user.component';
import { CategoryComponent } from './admin/category/category.component';
import { AdminDashboardComponent } from './admin/admin-dashboard/admin-dashboard.component';
import { RemindersComponent } from './home/reminders/reminders.component';
import { ProfileComponent } from './home/profile/profile.component';
import { PaymentComponent } from './home/payment/payment.component';
import { UserDashboardComponent } from './home/user-dashboard/user-dashboard.component';
import { PremiumCategoryComponent } from './home/premium-category/premium-category.component';

const routes: Routes = [
  {
    path: '',
    component: LandingPageComponent
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'register',
    component: RegisterComponent
  },
  { 
    path: 'error', 
    component: ErrorComponent 
  },
  {
    path: 'logout',
    component: LogoutComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'admin',
    component: AdminComponent,
    canActivate: [AuthGuard, AdminGuard],
    canActivateChild: [AuthGuard, AdminGuard],
    children: [
      { path: 'user', component: UserComponent },
      { path: 'category', component: CategoryComponent },
      { path: 'dashboard', component: AdminDashboardComponent }
    ]
  },
  {
    path: 'home',
    component: HomeComponent,
    canActivate: [AuthGuard],
    canActivateChild: [AuthGuard],
    children: [
      { path: 'expense', component: ExpenseComponent },
      { path: 'reminders', component: RemindersComponent },
      { path: 'profile', component: ProfileComponent },
      { path: 'to-premium', component: PaymentComponent },
      { path: 'u-dashboard', component: UserDashboardComponent },
      { path: 'p-category', component: PremiumCategoryComponent }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
