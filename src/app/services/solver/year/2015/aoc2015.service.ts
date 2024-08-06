import { Injectable } from '@angular/core';
import { getCombinations } from '../../helpers'

@Injectable({
  providedIn: 'root'
})
export class Aoc2015Service {

  constructor() { }

  /**
   * Day 1: Not Quite Lisp
   * @param input {string} - The input string.
   * @returns {[number, number]} - [Part One, Part Two] solution.
   */
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

  /**
   * Day 2: I Was Told There Would Be No Math
   * @param input {string} - The input string.
   * @returns {[number, number]} - [Part One, Part Two] solution.
   */
  day2(input: string): [number, number] {
    const readInput = (data: string): number[][] => {
      const lines: string[] = input.split("\n");
      const inputData: number[][] = [];
      for (const line of lines) {
        inputData.push(line.split("x").map(Number));
      }
      return inputData;
    }

    const lines = readInput(input)
    let areaSum: number = 0;
    let periVolSum: number = 0;

    for (const line of lines) {
      let c: number[][] = getCombinations(line, 2);

      const areas: number[] = c.map((x) => x[0] * x[1]);
      const areasT: number[] = areas.map((x) => 2 * x);

      c = getCombinations(line, 2);
      const perimeters: number[] = c.map((x) => 2 * x[0] + 2 * x[1])
      const volume: number = line[0] * line[1] * line[2];

      periVolSum += Math.min.apply(Math, perimeters) + volume

      areaSum += areasT.reduce((acc, value) => acc + value, 0) + Math.min.apply(Math, areas)
    }

    return [areaSum, periVolSum]
  }
}
