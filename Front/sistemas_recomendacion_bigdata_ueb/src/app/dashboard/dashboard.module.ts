import {NgModule} from '@angular/core';

import {DashboardRoutingModule} from './dashboard-routing.module';

import {SharedModule} from '../shared/shared.module';
import {HomeComponent} from './home/home.component';
import {DashboardService} from './dashboard.service';


@NgModule({
  declarations: [
    HomeComponent
  ],
  imports: [
    SharedModule,
    DashboardRoutingModule,
  ],
  providers: [
    DashboardService
  ]
})
export class DashboardModule {
}
