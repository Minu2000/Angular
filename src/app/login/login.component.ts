import { Component } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username:string ='';
  email: string ='';
  password: string='';



constructor(private http: HttpClient, private router: Router) {}
login(){
  const url = 'http://localhost:5000/api/v1/login'; 
    const loginData = {
      username:this.username,
      email: this.email,
      password: this.password
    };

this.http.post(url, loginData)
.subscribe(
  {
    next:  response => console.log(response),
    error: error=>console.log(error),
    //this.router.navigate(['/dashboard']);
  },
);
}
}
