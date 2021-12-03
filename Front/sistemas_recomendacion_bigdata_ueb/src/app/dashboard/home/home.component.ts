import {Component, OnInit} from '@angular/core';
import {DashboardService} from '../dashboard.service';

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

  getVideoGames(): void {
    this._dashboardService.getRecommenderVideogames().subscribe((response) => {

        console.log('success:', response);

        this.listVideogames = response.message;

      }, (error) => {
        console.error(error, 'Ha ocurrido un error.');
      }
    )
  }

  likeVideogame(index: any): void {
    this.listVideogames[index].Puntuacion = 1;
  }

  dislikeVideogame(index: any): void {
    this.listVideogames[index].Puntuacion = -1;
  }

  clearScoreVideogame(index: any): void {
    this.listVideogames[index].Puntuacion = -0;
  }

  getPuntuacion(index: any): any {
    console.log(this.listVideogames[index].Puntuacion);
    return this.listVideogames[index].Puntuacion;
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Private methods
  // ----------------------------------------------------------------------------------------------------


}
