import { TestBed } from '@angular/core/testing';

import { Aoc2023Service } from './aoc2023.service';

describe('Aoc2023Service', () => {
  let service: Aoc2023Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2023Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
