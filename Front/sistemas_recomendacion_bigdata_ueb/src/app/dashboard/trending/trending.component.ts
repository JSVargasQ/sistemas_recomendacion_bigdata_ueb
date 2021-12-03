import {Component, OnInit} from '@angular/core';
import {DashboardService} from '../dashboard.service';
import {AuthService} from '../../auth/auth.service';

@Component({
  selector: 'app-trending',
  templateUrl: './trending.component.html',
  styleUrls: ['./tendring.component.css']
})
export class TrendingComponent implements OnInit {


  // -----------------------------------------------------------------------------------------------------
  // @ Attributes
  // ----------------------------------------------------------------------------------------------------

  myListFavoriteVideogames: any[];

  // -----------------------------------------------------------------------------------------------------
  // @ Constructor
  // ----------------------------------------------------------------------------------------------------

  constructor(
    private _dashboardService: DashboardService,
    private _authService: AuthService
  ) {

  }

  // -----------------------------------------------------------------------------------------------------
  // @ Life Cycle
  // ----------------------------------------------------------------------------------------------------

  ngOnInit() {
    this.getFavoriteVideoGames();
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // ----------------------------------------------------------------------------------------------------

  getFavoriteVideoGames(): void {
    this._dashboardService.getRecommendationUser( this._authService.userLocalStorage.cod_usuario ).subscribe((response) => {
        console.log('success:', response);

        this.myListFavoriteVideogames = response.message;
      }, (error) => {
        console.error(error, 'Ha ocurrido un error.');
      }
    )
  }

  likeVideogame(videogame:any, index: any): void {
    console.log(videogame);
    if (this.myListFavoriteVideogames[index].isSelected === true) {
      this.myListFavoriteVideogames[index].isSelected = false;
      this.myListFavoriteVideogames[index].puntuacion = 0;
      this._dashboardService.rateVideogame(
        this._authService.userLocalStorage.cod_usuario,
        videogame.Num,
        0
      ).subscribe((response) => {
        console.log('response', response);
      });
    } else {
      this.myListFavoriteVideogames[index].isSelected = true
      this.myListFavoriteVideogames[index].puntuacion = 1;
      this._dashboardService.rateVideogame(
        this._authService.userLocalStorage.cod_usuario,
        videogame.Num,
        1
      ).subscribe((response) => {
        console.log('response', response);
      });
    }
    console.log(this.myListFavoriteVideogames[index]);
    console.log(videogame);
  }

  dislikeVideogame(videogame: any, index: any): void {
    console.log(videogame);
    if (this.myListFavoriteVideogames[index].puntuacion === -1) {
      this.myListFavoriteVideogames[index].puntuacion = 0;
      this._dashboardService.rateVideogame(
        this._authService.userLocalStorage.cod_usuario,
        videogame.Num,
        0
      ).subscribe((response) => {
        console.log('response', response);
      });
    } else {
      this.myListFavoriteVideogames[index].puntuacion = -1;
      this.myListFavoriteVideogames[index].isSelected = false;
      this._dashboardService.rateVideogame(
        this._authService.userLocalStorage.cod_usuario,
        videogame.Num,
        -1
      ).subscribe((response) => {
        console.log('response', response);
      });
    }
    console.log(videogame);
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Private methods
  // ----------------------------------------------------------------------------------------------------


}
