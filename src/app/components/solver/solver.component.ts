import { Component, ElementRef, ViewChild } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { SolverService } from '../../services/solver/solver.service';

@Component({
  selector: 'app-solver',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './solver.component.html',
  styleUrl: './solver.component.css'
})
export class SolverComponent {
  @ViewChild('ansModal') ansModal!: ElementRef;

  eventYear: number = 0;
  eventDay: number = 0;
  input: string = '';
  partOne: string = '';
  partTwo: string = '';

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

  solve() {
    if (this.input === '') {
      this.ansModal.nativeElement.showModal();
      return;
    }

    const solver = new SolverService();
    const solverFunction = solver.getFunction(this.eventYear, this.eventDay);

    const result = solverFunction(this.input);
    this.partOne = result[0];
    this.partTwo = result[1];

    this.ansModal.nativeElement.showModal();
  }
}