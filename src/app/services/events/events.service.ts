import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, distinct, map } from 'rxjs';
import { Event, EventDay } from '../../interfaces/events';
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

  getEventDays(year: number): Observable<EventDay[]> {
    return this.http.get<EventDay[]>('../../../../assets/year/' + year.toString() + '.json');
  }

  getEventDay(year: number, day: number): Observable<EventDay | undefined> {
    return this.getEventDays(year).pipe(
      map(days => {
        return days.find(D => D.day === day);
      })
    );
  }
}
