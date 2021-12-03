import {Injectable} from '@angular/core';
import {BehaviorSubject, Observable, Subscription} from 'rxjs';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {environment} from 'src/environments/environment';
import {User} from './auth.types';
import {tap} from 'rxjs/operators';
import {Router} from '@angular/router';


@Injectable()
export class AuthService {

  // -----------------------------------------------------------------------------------------------------
  // @ Attributes
  // ----------------------------------------------------------------------------------------------------
  private readonly API_URL = environment.apiUrl;

  serviceLoading = false;

  private _currentUser: BehaviorSubject<User> = new BehaviorSubject(null);


  // -----------------------------------------------------------------------------------------------------
  // @ Constructor
  // -----------------------------------------------------------------------------------------------------

  constructor(
    private _http: HttpClient,
    private _router: Router
  ) {
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Accessors
  // -----------------------------------------------------------------------------------------------------

  get currentUser$(): Observable<any> {
    return this._currentUser.asObservable();
  }

  set currentUser(value: any) {
    this._currentUser.next(value);
  }

  get userLocalStorage(): any {
    return JSON.parse(localStorage.getItem('USER_SIST_RECOMEN'));
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // -----------------------------------------------------------------------------------------------------

  signIn(user: User): Observable<any> {
    return this._http
      .post(this.API_URL + 'login/', user)
      .pipe(
        tap((response) => {
          if (response && response.status && response.status === 'Success') {

            user.cod_usuario = response.cod_usuario;

            this._currentUser.next(user);
            this._saveUserLocalStorage(user.correo, user.cod_usuario);

            this._router.navigate(['./dashboard']);
          } else {
            console.error('Error usu y contraseña');
          }

        })
      )
  }

  registerUser(user: User): Observable<any> {
    return this._http.post(this.API_URL + 'usuarios/', user);
  }

  getAllUsers(): void {
    this._http.get<any>(this.API_URL + 'usuarios/').subscribe(
      (response) => {
        console.log(response);
      },
      (error: HttpErrorResponse) => {
        console.log(error.name + ' ' + error.message);
      }
    );
  }

  clearSessionData(): void {
    this._currentUser.next(null);
    localStorage.removeItem('USER_SIST_RECOMEN');
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Private methods
  // -----------------------------------------------------------------------------------------------------

  private _saveUserLocalStorage(correo: string, codUsuario: number): void {
    localStorage.setItem('USER_SIST_RECOMEN', JSON.stringify({correo, cod_usuario: codUsuario}));
  }


}
