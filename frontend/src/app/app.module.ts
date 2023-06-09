import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReactiveFormsModule } from '@angular/forms';
import { AuthInterceptor } from './services/auth.interceptor';
import { ErrorComponent } from './error/error.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { HomeComponent } from './home/home.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { RegisterComponent } from './register/register.component';
import { ExpenseComponent } from './home/expense/expense.component';
import { AdminComponent } from './admin/admin.component';
import { CategoryComponent } from './admin/category/category.component';
import { UserComponent } from './admin/user/user.component';
import { AdminDashboardComponent } from './admin/admin-dashboard/admin-dashboard.component';
import { RemindersComponent } from './home/reminders/reminders.component';
import { ProfileComponent } from './home/profile/profile.component';
import { PaymentComponent } from './home/payment/payment.component';
import { UserDashboardComponent } from './home/user-dashboard/user-dashboard.component';
import { PremiumCategoryComponent } from './home/premium-category/premium-category.component';

@NgModule({
  declarations: [
    AppComponent,
    ErrorComponent,
    LoginComponent,
    LogoutComponent,
    HomeComponent,
    LandingPageComponent,
    RegisterComponent,
    ExpenseComponent,
    AdminComponent,
    CategoryComponent,
    UserComponent,
    AdminDashboardComponent,
    RemindersComponent,
    ProfileComponent,
    PaymentComponent,
    UserDashboardComponent,
    PremiumCategoryComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
