import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthService } from './auth.service';
import { Category } from '../category/category.model';

const appServer = 'http://localhost:5000';
const GET_CATEGORIES_FOR_ADMIN_API = '/api/category/getAllForAdmin';
const GET_CATEGORIES_FOR_USER_API = '/api/category/getAllForCurrentUser';
const ADD_CATEGORY_API = '/api/category/addCategory';
const EDIT_CATEGORY_API = '/api/category/editCategory';
const DELETE_CATEGORY_API = '/api/category/deleteCategory';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  constructor(private http: HttpClient, private authService: AuthService) {

  }

  getAllCategories() {
    let url: string;
    if (this.authService.isAdmin()) {
      url = appServer + GET_CATEGORIES_FOR_ADMIN_API;
    }
    else {
      url = appServer + GET_CATEGORIES_FOR_USER_API; 
    }

    return this.http.get(url);
  }

  addCategory(category: Category) {
    let url = appServer + ADD_CATEGORY_API;

    return this.http.post(url, category);
  }

  updateCategory(category) {
    const url = appServer + EDIT_CATEGORY_API;

    return this.http.post(url, category);
  }

  deleteCategory(categoryId: number) {
    let url = appServer + DELETE_CATEGORY_API;

    return this.http.post(url, {
      id: categoryId
    });
  }
}
