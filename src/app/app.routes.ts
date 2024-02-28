import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { SolverComponent } from './components/solver/solver.component';
import { EventComponent } from './components/event/event.component';

export const routes: Routes = [{
    path: '',
    component: HomeComponent
}, {
    path: ':year',
    component: EventComponent
}, {
    path: ':year/:day',
    component: SolverComponent
}, {
    path: '**',
    redirectTo: ''
}];
