import {Component, AfterViewInit, ViewChild, ElementRef} from '@angular/core';
import {createPopper} from '@popperjs/core';
import {AuthService} from "../../../auth/auth.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-user-dropdown',
  templateUrl: './user-dropdown.component.html'
})
export class UserDropdownComponent implements AfterViewInit {
  dropdownPopoverShow = false;
  @ViewChild('btnDropdownRef', {static: false}) btnDropdownRef: ElementRef;
  @ViewChild('popoverDropdownRef', {static: false})
  popoverDropdownRef: ElementRef;

  constructor(
    private _authService: AuthService,
    private _router: Router,
  ) {
  }

  ngAfterViewInit() {
    createPopper(
      this.btnDropdownRef.nativeElement,
      this.popoverDropdownRef.nativeElement,
      {
        placement: 'bottom-start',
      }
    );
  }

  toggleDropdown(event) {
    event.preventDefault();
    if (this.dropdownPopoverShow) {
      this.dropdownPopoverShow = false;
    } else {
      this.dropdownPopoverShow = true;
    }
  }

  signOut(): void {
    this._router.navigate(['/auth/signin']);
    console.log('cerrando...');

    this._authService.clearSessionData();
  }
}
