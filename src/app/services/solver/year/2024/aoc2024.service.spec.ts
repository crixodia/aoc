import { TestBed } from '@angular/core/testing';

import { Aoc2024Service } from './aoc2024.service';

describe('Aoc2024Service', () => {
  let service: Aoc2024Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2024Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
