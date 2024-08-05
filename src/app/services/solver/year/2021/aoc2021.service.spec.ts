import { TestBed } from '@angular/core/testing';

import { Aoc2021Service } from './aoc2021.service';

describe('Aoc2021Service', () => {
  let service: Aoc2021Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Aoc2021Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
