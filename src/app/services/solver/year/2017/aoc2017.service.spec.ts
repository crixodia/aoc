import { TestBed } from '@angular/core/testing';

import { Aoc2017Service } from './aoc2017.service';

describe('Aoc2017Service', () => {
  let service: Aoc2017Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2017Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
