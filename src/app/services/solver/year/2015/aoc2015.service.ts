import { Injectable } from '@angular/core';
import { getCombinations, addArrs, containsArray } from '../../helpers'
import { Md5 } from 'ts-md5';

@Injectable({
  providedIn: 'root'
})
export class Aoc2015Service {

  constructor() { }

  /**
   * Day 1: Not Quite Lisp
   * @param input {string} - The input string.
   * @returns {[number, number]} - [Part One, Part Two] solution.
   * @see https://adventofcode.com/2015/day/1
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
   * @see https://adventofcode.com/2015/day/2
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

  /**
   * Day 3: Perfectly Spherical Houses in a Vacuum
   * @param input {string} - The input string.
   * @returns {[number, number]} - [Part One, Part Two] solution.
   * @see https://adventofcode.com/2015/day/3
   */
  day3(input: string): [number, number] {
    const moves: { [key: string]: number[] } = { ">": [1, 0], "v": [0, -1], "<": [-1, 0], "^": [0, 1] };

    const partOne = (instructions: string): number[][] => {
      let current: number[] = [0, 0];
      let positions: number[][] = [current];
      for (const c of instructions) {
        current = addArrs(moves[c], current);
        if (!containsArray(positions, current)) {
          positions.push(current);
        }
      }
      return positions;
    }

    const partTwo = (instructions: string): number[][] => {
      let instructionsA: string = "";
      let instructionsB: string = "";
      let current: number[] = [0, 0];
      let positions: number[][] = [current];

      for (let i = 0; i < instructions.length; i++) {
        if (i % 2 == 0) {
          instructionsA += instructions[i]
        } else {
          instructionsB += instructions[i]
        }
      }

      const iAB: string[] = [instructionsA, instructionsB];
      for (const I of iAB) {
        current = [0, 0];
        for (const c of I) {
          current = addArrs(current, moves[c]);
          if (!containsArray(positions, current)) {
            positions.push(current);
          }
        }
      }
      return positions;
    }

    return [partOne(input).length, partTwo(input).length]
  }

  /**
   * Day 4: The Ideal Stocking Stuffer
   * @param input {string} - The input string.
   * @returns {[number, number]} - [Part One, Part Two] solution.
   * @see https://adventofcode.com/2015/day/4
   */
  day4 = (input: string): number[] => {
    const solve = (input: string, times: number): number => {
      let i: number = 0;
      let z: string = "";

      for (let j = 0; j < times; j++) {
        z += "0";
      }

      for (; i < 10000000; i++) {
        const to_hash_tmp: string = input + i.toString();
        const hash: string = Md5.hashStr(to_hash_tmp);
        if (hash.startsWith(z)) {
          return i
        }
      }
      return -1;
    }

    return [solve(input, 5), solve(input, 6)];
  }

  /**
   * Day 5: Doesn't He Have Intern-Elves For This?
   * @param input {string} - The input string.
   * @returns {[number, number]} - [Part One, Part Two] solution.
   * @see https://adventofcode.com/2015/day/5
   */
  day5 = (input: string): number[] => {
    const readInput = (input: string): string[] => {
      return input.split("\n");
    }

    const partOne = (s: string): number => {
      let vc: number = 0;
      let vowelFlag: boolean = false;
      let lastTwo: string[] = ["", ""];
      const vowels: string[] = ["a", "e", "i", "o", "u"];
      const twoCondition: string[] = ["ab", "cd", "pq", "xy"];

      for (const c of s) {
        lastTwo.push(c);
        lastTwo.shift();

        if (twoCondition.includes(lastTwo.join(""))) return 0;
        if (lastTwo.join("") === c + c) vowelFlag = true;
        if (vowels.includes(c)) vc++;
      }

      return Number(vc >= 3 && vowelFlag);
    }

    const partTwo = (s: string): number => {
      let c1: boolean = false;
      let c2: boolean = false;

      for (let i = 0; i < s.length; i++) {
        if (i + 2 >= s.length) continue;
        if (s[i] === s[i + 2]) c2 = true;

        for (let j = i + 2; j < s.length; j++)
          if (s.substring(i, i + 2) === s.substring(j, j + 2)) c1 = true;
      }
      return Number(c1 && c2);
    }

    let s1: number = 0;
    let s2: number = 0;
    for (const r of readInput(input)) {
      s1 += partOne(r);
      s2 += partTwo(r);
    }

    return [s1, s2];
  }
}
