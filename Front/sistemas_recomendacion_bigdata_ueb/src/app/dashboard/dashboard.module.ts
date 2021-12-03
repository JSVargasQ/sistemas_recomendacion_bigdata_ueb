import {NgModule} from '@angular/core';

import {DashboardRoutingModule} from './dashboard-routing.module';

import {SharedModule} from '../shared/shared.module';
import {HomeComponent} from './home/home.component';
import {DashboardService} from './dashboard.service';
import {AuthService} from '../auth/auth.service';
import {LikesComponent} from './likes/likes.component';
import {DashboardGuard} from './dashboard.guard';
import {TrendingComponent} from './trending/trending.component';


@NgModule({
  declarations: [
    HomeComponent,
    LikesComponent,
    TrendingComponent
  ],
  imports: [
    SharedModule,
    DashboardRoutingModule,
  ],
  providers: [
    AuthService,
    DashboardService,
    DashboardGuard
  ]
})
export class DashboardModule {
}
