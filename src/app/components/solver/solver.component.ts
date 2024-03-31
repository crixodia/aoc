import { Component } from '@angular/core';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-solver',
  standalone: true,
  imports: [],
  templateUrl: './solver.component.html',
  styleUrl: './solver.component.css'
})
export class SolverComponent {
  eventYear: number = 0;
  eventDay: number = 0;

  constructor(private route: ActivatedRoute, private router: Router) { }

  ngOnInit() {
    this.eventYear = Number(this.route.snapshot.paramMap.get('year'));
    this.eventDay = Number(this.route.snapshot.paramMap.get('day'));

    if (this.eventDay < 1 || this.eventDay > 25) {
      this.router.navigate(['/', this.eventYear.toString()]);
    }
  }

  navigateCancel() {
    this.router.navigate(['/', this.eventYear.toString()]);
  }
}
