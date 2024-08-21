import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { SolverComponent } from './components/solver/solver.component';
import { EventComponent } from './components/event/event.component';

export const routes: Routes = [{
    path: '',
    component: HomeComponent,
    title: 'Advent of Code Solver'
}, {
    path: ':year',
    component: EventComponent,
    title: 'Advent of Code Solver | Calendar'
}, {
    path: ':year/:day',
    component: SolverComponent,
    title: 'Advent of Code Solver | Day'
}, {
    path: '**',
    redirectTo: ''
}];
