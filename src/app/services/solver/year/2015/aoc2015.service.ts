import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class Aoc2015Service {

  constructor() { }

  day1(input: string): [number, number] {
    const readInput = (data: string): string[] => {
      const s: string[] = [];
      for (const c of data) {
        s.push(c);
      }
      return s;
    }

    const instruction: { [key: string]: number } = { '(': 1, ')': -1 };
    let sum = 0;
    let pos = 0;

    const transformed_input = readInput(input);

    transformed_input.forEach((char, index) => {
      sum += instruction[char];
      if (sum === -1 && pos === 0) {
        pos = index + 1;
      }
    });
    return [sum, pos];
  }
}
