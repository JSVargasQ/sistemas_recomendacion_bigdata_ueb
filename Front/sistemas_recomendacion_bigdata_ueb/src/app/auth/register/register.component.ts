import {Component, OnInit} from '@angular/core';
import {AuthService} from '../auth.service';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {User} from '../auth.types';
import {Router} from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  // -----------------------------------------------------------------------------------------------------
  // @ Attributes
  // ----------------------------------------------------------------------------------------------------

  maxDateRegister: any;

  formRegister: FormGroup;

  // -----------------------------------------------------------------------------------------------------
  // @ Constructor
  // ----------------------------------------------------------------------------------------------------

  constructor(
    private _authService: AuthService,
    private _formBuilder: FormBuilder,
    private _router: Router
  ) {

  }

  // -----------------------------------------------------------------------------------------------------
  // @ Life Cycle
  // ----------------------------------------------------------------------------------------------------

  ngOnInit() {
    const now = new Date();
    this.maxDateRegister = (now.getFullYear() - 18) + '-' + now.getMonth() + '-' + (now.getDay() < 10 ? '0' : '') + now.getDay();
    console.log(this.maxDateRegister);

    this._initForm();
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // ----------------------------------------------------------------------------------------------------

  registerUser(): void {
    this.formRegister.disable();

    const user: User = this.formRegister.value;
    user.fecha_nacimiento = user.fecha_nacimiento.split('/').join('-') ;

    this._authService.registerUser(user).subscribe((response) => {

      console.log('success:', response);

      if ( response && response.status === 'Success') {
        this._router.navigate(['./auth/signin'])
      }

      this.formRegister.enable();

      }, (error) => {
        console.error(error, 'Ha ocurrido un error.');
      }
    )
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Private methods
  // ----------------------------------------------------------------------------------------------------

  private _initForm(): void {
    this.formRegister = this._formBuilder.group({
      correo: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]],
      confirm_password: ['', Validators.required],
      nombre_usuario: ['', Validators.required],
      pais: ['', Validators.required],
      fecha_nacimiento: ['', [Validators.required]]
    });
  }


}
