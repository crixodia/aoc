import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, distinct, map } from 'rxjs';
import { Event } from '../../interfaces/events';
@Injectable({
  providedIn: 'root'
})
export class EventsService {

  constructor(private http: HttpClient) { }

  getEvents(): Observable<Event[]> {
    return this.http.get<Event[]>('../../../../assets/events.json');
  }

  getEventsYearList(): Observable<number[]> {
    return this.getEvents().pipe(
      map(events => {
        return events.map(event => event.year);
      }),
      distinct()
    );
  }
}
