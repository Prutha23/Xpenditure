import { Component, OnInit } from '@angular/core';
import { CategoryService } from '../services/category.service';
import { Category } from './category.model';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {

  form: FormGroup;

  editMode: boolean = false;

  categories: Category[];

  selectedCategory: Category = null;

  constructor(private categoryService: CategoryService) {

  }

  ngOnInit(): void {
    this.form = new FormGroup({
      'name': new FormControl('', Validators.required),
      'remarks': new FormControl('', Validators.required)
    });
    this.fetchCategories();
  }

  private fetchCategories() {
    this.categoryService.getAllCategories().subscribe({
      next: res => {
        console.log(res);
        if (res['statusCode'] === 200) {
          this.categories = res['data'];
        }
      }
    });
  }

  onCategoryToggle(category: Category) {
    this.selectedCategory = category;
    this.form.patchValue({
      'name': this.selectedCategory.NAME,
      'remarks': this.selectedCategory.REMARKS
    });
    this.editMode = true;
  }

  onSubmit() {
    let observable: Observable<any>;
    if (this.editMode) {
      observable = this.categoryService.updateCategory({
        id: this.selectedCategory.ID,
        name: this.form.value.name,
        remarks: this.form.value.remarks
      });
    }
    else {
      observable = this.categoryService.addCategory(this.form.value);
    }
    observable.subscribe({
      next: res => {
        if (res['statusCode'] === 200) {
          this.fetchCategories();
          this.onClear();
        }
      }
    })
  }

  onClear() {
    this.form.reset();
    this.editMode = false;
  }

  onDelete() {
    this.categoryService.deleteCategory(this.selectedCategory.ID).subscribe({
      next: res => {
        console.log(res);
        if (res['statusCode'] === 200) {
          this.fetchCategories();
          this.onClear();
        }
      }
    });
  }
}
