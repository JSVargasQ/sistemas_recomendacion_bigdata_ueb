import {Component, OnInit} from '@angular/core';
import {DashboardService} from '../dashboard.service';
import {AuthService} from '../../auth/auth.service';

@Component({
  selector: 'app-like',
  templateUrl: './likes.component.html',
  styleUrls: ['./likes.component.css']
})
export class LikesComponent implements OnInit {


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
    this._dashboardService.getMyFavoriteVideogames(this._authService.userLocalStorage.cod_usuario).subscribe((response) => {
        console.log('success:', response);

        if ((typeof response.message) === 'object') {
          this.myListFavoriteVideogames = response.message;
        } else {
          this.myListFavoriteVideogames = [];
        }
      }, (error) => {
        console.error(error, 'Ha ocurrido un error.');
      }
    )
  }

  dislikeVideogame(videogame: any, index: any): void {
    if (this.myListFavoriteVideogames[index].Puntuacion === -1) {
      this.myListFavoriteVideogames[index].Puntuacion = 0;
      this._dashboardService.rateVideogame(
        this._authService.userLocalStorage.cod_usuario,
        videogame.Num,
        0
      ).subscribe((response) => {
        console.log('response', response);
      });
    } else {
      this.myListFavoriteVideogames[index].Puntuacion = -1;
      this.myListFavoriteVideogames[index].isSelected = false;
      this._dashboardService.rateVideogame(
        this._authService.userLocalStorage.cod_usuario,
        videogame.Num,
        -1
      ).subscribe((response) => {
        console.log('response', response);
      });
    }
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Private methods
  // ----------------------------------------------------------------------------------------------------


}
