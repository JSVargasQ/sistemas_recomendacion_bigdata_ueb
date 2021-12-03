import {Injectable} from '@angular/core';
import {BehaviorSubject, Observable, Subscription} from 'rxjs';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {environment} from 'src/environments/environment';
import {tap} from 'rxjs/operators';


@Injectable()
export class DashboardService {

  // -----------------------------------------------------------------------------------------------------
  // @ Attributes
  // ----------------------------------------------------------------------------------------------------
  private readonly API_URL = environment.apiUrl;


  // -----------------------------------------------------------------------------------------------------
  // @ Constructor
  // -----------------------------------------------------------------------------------------------------

  constructor(private _http: HttpClient) {
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Accessors
  // -----------------------------------------------------------------------------------------------------

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // ----------------------------------------------------------------------------------------------------

  getRandomVideogames(): Observable<any> {
    return this._http.get<any>(this.API_URL + 'peliculas/');
  }

  getRecommendationContent(body): Observable<any> {
    return this._http.post<any>(this.API_URL + 'peliculas/', body);
  }

  getRecommendationUser(codUsuario: number): Observable<any> {
    return this._http.get<any>(this.API_URL + 'recomendacionUsuario/' + codUsuario);
  }

  getMyFavoriteVideogames(codUsuario: number): Observable<any> {
    return this._http.get<any>(this.API_URL + 'calificaciones/' + codUsuario);
  }

  rateVideogame(codUser: number, codVideogame: number, puntuacion: number): Observable<any> {
    return this._http.post<any>(this.API_URL + 'peliculas/',
      {
        usuario: codUser,
        juegos: [{
          Num: codVideogame,
          Puntuacion: puntuacion
        }]
      });
  }

}
