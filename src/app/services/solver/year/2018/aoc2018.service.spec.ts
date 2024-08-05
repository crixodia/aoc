import { TestBed } from '@angular/core/testing';

import { Aoc2018Service } from './aoc2018.service';

describe('Aoc2018Service', () => {
  let service: Aoc2018Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2018Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
