import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';

@Injectable()
export class AuthGuard implements CanActivate {

    constructor(private router: Router) { }

    canActivate(): boolean {
        if (localStorage.getItem('isLoggedin')) {
            // logged in so return true
            return true;
        }

        this.router.navigate(['/login']);
        return false;
    }
}

