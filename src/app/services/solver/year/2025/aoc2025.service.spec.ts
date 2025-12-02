import { TestBed } from '@angular/core/testing';

import { Aoc2025Service } from './aoc2025.service';

describe('Aoc2025Service', () => {
  let service: Aoc2025Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2025Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
