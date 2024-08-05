import { TestBed } from '@angular/core/testing';

import { Aoc2022Service } from './aoc2022.service';

describe('Aoc2022Service', () => {
  let service: Aoc2022Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2022Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
