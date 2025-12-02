import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class Aoc2025Service {

  constructor() { }
  /**
 * Day 1: Secret Entrance
 * @param input {string} - The input string.
 * @returns {[number, number]} - [Part One, Part Two] solution.
 * @see https://adventofcode.com/2025/day/1
 */
  day1(input: string): [number, number] {
    const readInput = (data: string): number[] => {
      const doc: string[] = data.split('\n');
      const result: number[] = doc
        .filter(line => line.trim() !== '')
        .map((instruction: string) => {
          if (instruction.length < 2) {
            return 0;
          }

          const direction: string = instruction[0];
          const magnitudeStr: string = instruction.substring(1);
          const magnitude: number = parseInt(magnitudeStr, 10);

          if (isNaN(magnitude)) {
            return 0;
          }

          if (direction === 'L') {
            return -1 * magnitude;
          } else {
            return magnitude;
          }
        });

      return result;
    }

    const solve = (puzzle: number[]): number => {
      let dialPos: number = 50;
      let zeroPointing: number = 0;
      let MODULO: number = 100;
      for (const ins of puzzle) {
        let newPos = dialPos + ins;
        dialPos = ((newPos % MODULO) + MODULO) % MODULO;
        if (dialPos === 0) {
          zeroPointing += 1;
        }
      }
      return zeroPointing;
    }

    const solve2 = (puzzle: number[]): number => {
      let dialPos: number = 50;
      let allZeroPointing: number = 0;

      for (const ins of puzzle) {
        const sign: number = ins < 0 ? -1 : 1;
        const magnitude: number = Math.abs(ins);

        for (let i = 0; i < magnitude; i++) {
          dialPos += sign * 1;
          if (dialPos === 100) {
            dialPos = 0;
          }
          else if (dialPos === -1) {
            dialPos = 99;
          }
          if (dialPos === 0) {
            allZeroPointing += 1;
          }
        }
      }

      return allZeroPointing;
    }

    const transformed_input = readInput(input);
    return [solve(transformed_input), solve2(transformed_input)];
  }

  /**
 * Day 2: Gift Shop
 * @param input {string} - The input string.
 * @returns {[number, number]} - [Part One, Part Two] solution.
 * @see https://adventofcode.com/2025/day/2
 */
  day2(input: string): [number, number] {
    const readInput = (data: string): [number, number][] => {
      const ranges: string[] = data.replace(/\n/g, '').split(',');
      const result: [number, number][] = ranges
        .filter(r => r.trim() !== '')
        .map((r): [number, number] => {
          const parts = r.split('-');
          if (parts.length === 2) {
            return [parseInt(parts[0], 10), parseInt(parts[1], 10)];
          }
          return [0, 0];
        })
        .filter((range): range is [number, number] => range[0] <= range[1]);

      return result;
    }

    const isInvalidId = (number: number): boolean => {
      const strNumber: string = String(number);
      const n: number = strNumber.length;

      if (n % 2 !== 0) {
        return false;
      }

      const halfLength: number = n / 2;
      const a: string = strNumber.substring(0, halfLength);
      const b: string = strNumber.substring(halfLength);

      return a === b;
    }

    const isInvalidAll = (number: number): boolean => {
      const strNumber: string = String(number);
      const n: number = strNumber.length;

      const multiples: number[] = [];
      for (let i = 1; i < n; i++) {
        if (n % i === 0) {
          multiples.push(i);
        }
      }

      for (const m of multiples) {
        const chunks: string[] = [];
        for (let i = 0; i < n; i += m) {
          chunks.push(strNumber.substring(i, i + m));
        }
        if (new Set(chunks).size === 1) {
          return true;
        }
      }

      return false;
    }

    const solve = (puzzle: [number, number][]): [number, number] => {
      let sumInvalid: number = 0;
      let sumInvalid2: number = 0;

      for (const [l, r] of puzzle) {
        for (let num = l; num <= r; num++) {
          if (isInvalidId(num)) {
            sumInvalid += num;
          }
          if (isInvalidAll(num)) {
            sumInvalid2 += num;
          }
        }
      }

      return [sumInvalid, sumInvalid2];
    }

    const transformedInput = readInput(input);
    return solve(transformedInput);
  }
}
