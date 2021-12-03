import {Component, OnInit} from '@angular/core';
import {DashboardService} from '../dashboard.service';
import {AuthService} from '../../auth/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {


  // -----------------------------------------------------------------------------------------------------
  // @ Attributes
  // ----------------------------------------------------------------------------------------------------

  listVideogames: any[];

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
    this.getVideoGames();
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // ----------------------------------------------------------------------------------------------------

  likeVideogame(index: any): void {

    if (this.listVideogames[index].isSelected === true) {
      this.listVideogames[index].isSelected = false;
      this.listVideogames[index].Puntuacion = 0;
    } else {
      this.listVideogames[index].isSelected = true
      this.listVideogames[index].Puntuacion = 1;
    }
    console.log(this.listVideogames[index]);
  }

  getVideoGames(): void {
    this._dashboardService.getRandomVideogames().subscribe((response) => {

        console.log('success:', response);

        response.message.forEach((element) => {
          element.Puntuacion = 0;
        });

        this.listVideogames = response.message;
      }, (error) => {
        console.error(error, 'Ha ocurrido un error.');
      }
    )
  }

  recommenderMore(): void {

    const juegos = [];

    this.listVideogames.forEach((videogame) => {
      juegos.push({
        Num: videogame.Num,
        Puntuacion: videogame.Puntuacion
      });
    });

    const body = {
      juegos,
      usuario: this._authService.userLocalStorage.cod_usuario
    };
    console.log(body);

    this._dashboardService.getRecommendationContent(body).subscribe((response) => {

        console.log('success:', response);

        response.message.forEach((element) => {
          element.Puntuacion = 0;
        });

        this.listVideogames = response.message

      }, (error) => {
        console.error(error, 'Ha ocurrido un error.');
      }
    )
  }

  dislikeVideogame(index: any): void {
    if (this.listVideogames[index].Puntuacion === -1) {
      this.listVideogames[index].Puntuacion = 0;
    } else {
      this.listVideogames[index].Puntuacion = -1;
      this.listVideogames[index].isSelected = false;
    }
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Private methods
  // ----------------------------------------------------------------------------------------------------


}
