import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterModule} from '@angular/router';

import {
  FooterComponent,
  NavbarComponent,
  SidebarComponent,
  UserDropdownComponent,
  NotificationDropdownComponent
} from './components';


@NgModule({
  declarations: [
    FooterComponent,
    NavbarComponent,
    SidebarComponent,
    UserDropdownComponent,
    NotificationDropdownComponent
  ],
  imports: [
    CommonModule,
    RouterModule,
  ],
  exports: [
    NavbarComponent,
    FooterComponent,
    SidebarComponent,
    CommonModule,
    RouterModule,
  ]
})
export class SharedModule {
}
