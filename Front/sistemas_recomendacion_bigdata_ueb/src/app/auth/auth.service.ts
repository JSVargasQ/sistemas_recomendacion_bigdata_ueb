import {Injectable} from '@angular/core';
import {BehaviorSubject, Observable, Subscription} from 'rxjs';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {environment} from 'src/environments/environment';
import {User} from './auth.types';
import {tap} from 'rxjs/operators';


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

  constructor(private _http: HttpClient) {
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

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // -----------------------------------------------------------------------------------------------------

  signIn(user: User): Observable<any> {
    return this._http
      .post(this.API_URL + 'usuarios/', user)
      .pipe(
        tap((response) => {
          this._currentUser.next(response);
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


}
