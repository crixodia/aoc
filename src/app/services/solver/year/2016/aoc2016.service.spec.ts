import { TestBed } from '@angular/core/testing';

import { Aoc2016Service } from './aoc2016.service';

describe('Aoc2016Service', () => {
  let service: Aoc2016Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2016Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
