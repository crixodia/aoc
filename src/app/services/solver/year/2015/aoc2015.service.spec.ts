import { TestBed } from '@angular/core/testing';

import { Aoc2015Service } from './aoc2015.service';

describe('Aoc2015Service', () => {
  let service: Aoc2015Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2015Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
