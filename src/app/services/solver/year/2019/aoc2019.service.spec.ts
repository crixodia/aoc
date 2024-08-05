import { TestBed } from '@angular/core/testing';

import { Aoc2019Service } from '../aoc2019.service';

describe('Aoc2019Service', () => {
  let service: Aoc2019Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2019Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
