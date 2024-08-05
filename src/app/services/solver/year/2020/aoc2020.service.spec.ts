import { TestBed } from '@angular/core/testing';

import { Aoc2020Service } from './aoc2020.service';

describe('Aoc2020Service', () => {
  let service: Aoc2020Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2020Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
