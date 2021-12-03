import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {HomeComponent} from './home/home.component';
import {LikesComponent} from './likes/likes.component';
import {DashboardGuard} from './dashboard.guard';
import {TrendingComponent} from "./trending/trending.component";

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'home',
    component: HomeComponent,
    canActivate: [DashboardGuard],
    canDeactivate: [DashboardGuard]
  },
  {
    path: 'my-likes',
    component: LikesComponent,
    canActivate: [DashboardGuard],
    canDeactivate: [DashboardGuard]
  },
  {
    path: 'trending',
    component: TrendingComponent,
    canActivate: [DashboardGuard],
    canDeactivate: [DashboardGuard]
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DashboardRoutingModule {
}
