// import { Component } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// @Component({
//   selector: 'app-registeration',
//   templateUrl: './registeration.component.html',
//   styleUrls: ['./registeration.component.css']
// })
// export class RegisterationComponent {}
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
//import { Router } from '@angular/router';

@Component({
  selector: 'app-registeration',
  templateUrl: './registeration.component.html',
  styleUrls: ['./registeration.component.css']
})
export class RegisterationComponent {
  username: string ='';
  email: string ='';
  password: string ='';

  constructor(private http: HttpClient) { }

  registerUser() {
    const url = 'http://localhost:5000/api/v1/register';
    const registrationData = {
      username: this.username,
      email: this.email,
      password: this.password
    };

    this.http.post(url, registrationData)
      .subscribe(
       {
          next: response => console.log(response),
          //this.router.navigate(['/login'])
         
          error: error=> console.log(error),
         

        }
       
      );
  }
}
