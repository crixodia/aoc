import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule, Router } from '@angular/router';
import { EventsService } from '../../services/events/events.service';


@Component({
  selector: 'app-event',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './event.component.html',
  styleUrl: './event.component.css'
})
export class EventComponent implements OnInit {
  eventYear: number = 0;
  calendarNumbers: number[][] = [];
  calendarDisabled: boolean[][] = [];
  weekDayStart: number = 0;

  constructor(private route: ActivatedRoute, private router: Router, private eventService: EventsService) { }

  ngOnInit() {
    this.eventYear = Number(this.route.snapshot.paramMap.get('year'));
    this.loadCalendar();
  }

  loadCalendar() {
    this.weekDayStart = this.zellerCongruenceJulian(this.eventYear, 12);
    this.genCalendarNumbers(this.weekDayStart);
    this.eventService.getEventsYearList().subscribe({
      next: (data: any) => {
        if (data.indexOf(this.eventYear) === -1) {
          this.router.navigate(['/']);
        }
      },
      error: (error: any) => {
        // console.error('Error:', error);
      }
    });
  }

  changeYear(year: number) {
    if (year === 0) {
      this.router.navigate(['/']);
      return;
    }

    this.eventYear = year;
    this.router.navigate(['/' + this.eventYear.toString()]);
    this.loadCalendar();
  }

  zellerCongruenceJulian(year: number, month: number, day: number = 1) {
    if (month < 3) {
      month += 12;
      year--;
    }

    let q = day;
    let m = month;
    let k = year % 100;
    let j = Math.floor(year / 100);
    let h = (q + Math.floor((13 * (m + 1)) / 5) + k + Math.floor(k / 4) + Math.floor(j / 4) + 5 * j) % 7;

    return h;
  }

  genCalendarNumbers(weekDay: number) {
    // Frist week day is Fri or Sat -> 6 weeks
    let nRows = weekDay === 0 || weekDay === 6 ? 6 : 5;

    this.calendarNumbers = Array(nRows).fill(0).map(() => Array(7).fill(0));
    this.calendarDisabled = Array(nRows).fill(0).map(() => Array(7).fill(true));

    // 0 - 6 -> Sun - Sat index of the week
    weekDay = weekDay == 0 ? 6 : weekDay - 1;

    let row = 0;
    for (let i = weekDay - 1; i >= 0; i--) {
      this.calendarNumbers[row][i % 7] = 30 - (weekDay - i - 1);
    }

    let j: number = 1;
    for (let i = weekDay; i < 31 + weekDay; i++) {
      this.calendarNumbers[row][i % 7] = j;
      this.calendarDisabled[row][i % 7] = j > 25;
      j++;
      if (i % 7 == 6) {
        row++;
      }
    }

    if (row < nRows - 1) row++;
    j = 1;
    for (let i = 31 + weekDay; i < nRows * 7; i++) {
      this.calendarNumbers[row][i % 7] = j;
      j++;
    }
  }

  getDayLabel(day: number) {
    switch (day) {
      case 1:
        return 'Sunday';
      case 2:
        return 'Monday';
      case 3:
        return 'Tuesday';
      case 4:
        return 'Wednesday';
      case 5:
        return 'Thursday';
      case 6:
        return 'Friday';
      case 0:
        return 'Saturday';
      default:
        return '';
    }
  }

  navigateSolver(day: number) {
    this.router.navigate([this.eventYear, day.toString()]);
  }
}
