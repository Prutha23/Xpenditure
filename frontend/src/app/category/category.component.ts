import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { HttpService } from '../services/http.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {

  categories: any = []
  openModal: Boolean = false;
  
  categoryForm = new FormGroup({
    ID: new FormControl(0),
    NAME: new FormControl('', Validators.required),
    REMARKS: new FormControl('')
  });

  constructor(private http: HttpService, private router: Router) {}

  ngOnInit(): void {

    // get category data
    this.http.get('/category/getAllForAdmin').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.categories = res['data']
        }
        else
          this.router.navigate(['/error'])
      }),
      (err => {
        this.router.navigate(['/error'])
      })
    );
  }

  onSubmit(){
    let data = this.categoryForm.value;
    console.log(data)

    if(data["ID"] == null || data["ID"] == 0) {
      this.http.post('/category/addCategory', data).subscribe(
        (res => {
          if(res["statusCode"] == '200'){
            console.log(res)
          }
          else
            this.router.navigate(['/error'])
        }),
        (err => {
          this.router.navigate(['/error'])
        })
      );
    }
    else {
      this.http.post('/category/editCategory', data).subscribe(
        (res => {
          if(res["statusCode"] == '200'){
            console.log(res)
          }
          else
            this.router.navigate(['/error'])
        }),
        (err => {
          this.router.navigate(['/error'])
        })
      );
    }

    // load category data
    this.http.get('/category/getAllForAdmin').subscribe(
      (res => {
        if(res["statusCode"] == '200'){
          console.log(res)
          this.categories = res['data']
        }
        else
          this.router.navigate(['/error'])
      }),
      (err => {
        this.router.navigate(['/error'])
      })
    );
  }

  clean(){
    this.categoryForm.reset();
  }

  edit(cat: any){
    this.categoryForm.reset();
    this.categoryForm = new FormGroup({
      ID: new FormControl(cat["ID"]),
      NAME: new FormControl(cat["NAME"], Validators.required),
      REMARKS: new FormControl(cat["REMARKS"])
    });
  }
}
