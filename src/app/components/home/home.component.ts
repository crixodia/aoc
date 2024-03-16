import { Component } from '@angular/core';
import { EventsService } from '../../services/events/events.service';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { Event } from '../../interfaces/events';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [HttpClientModule, CommonModule],
  providers: [EventsService],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  events: Event[] = [];
  loadingImages: boolean[] = [];

  constructor(private eventsService: EventsService, private router: Router) {
    this.eventsService.getEvents().subscribe({
      next: (data: any) => {
        this.events = data;
        this.loadingImages = new Array(this.events.length).fill(true);
      },
      error: (error: any) => {
        // console.error('Error:', error);
      }
    });
  }

  navigateEvent(year: number) {
    this.router.navigate([year.toString()]);
  }
}
