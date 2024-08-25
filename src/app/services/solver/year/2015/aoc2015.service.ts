import { Injectable } from '@angular/core';
import { getCombinations, addArrs, containsArray, sumArray, isDecimal, getPermutations } from '../../helpers'
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

  /**
   * Day 6: Probably a Fire Hazard
   * @param input {string} - The input string.
   * @returns {[number, number]} - [Part One, Part Two] solution.
   */
  day6 = (input: string): number[] => {
    const readInput = (input: string): number[][] => {
      let parsedInput: number[][] = [];
      const lines: string[] = input.split("\n");
      for (const line of lines) {
        let temp: string = "";
        temp = line.replace(" through", ",");
        temp = temp.replace("turn on ", "1,");
        temp = temp.replace("turn off ", "-1,");
        temp = temp.replace("toggle ", "2,");

        parsedInput.push(temp.split(",").map((x) => Number(x)));
      }
      return parsedInput;
    }

    const partOne = (parsedInput: number[][]): number => {
      let grid: boolean[][] = Array.from({ length: 1000 }, () => Array(1000).fill(false));
      for (const row of parsedInput) {
        const [state, x, y, X, Y] = row;

        for (let i = x; i <= X; i++) {
          for (let j = y; j <= Y; j++) {
            if (state === 1) grid[i][j] = true;
            else if (state === -1) grid[i][j] = false;
            else grid[i][j] = !grid[i][j];
          }
        }
      }

      const sumGrid = grid.flat().reduce((sum, val) => sum + (val ? 1 : 0), 0);
      return sumGrid;
    }

    const partTwo = (parsedInput: number[][]): number => {
      let grid: number[][] = Array.from({ length: 1000 }, () => Array(1000).fill(0));
      for (const row of parsedInput) {
        const [state, x, y, X, Y] = row;

        for (let i = x; i <= X; i++) {
          for (let j = y; j <= Y; j++) {
            if (state === -1 && grid[i][j] === 0) continue;
            grid[i][j] = grid[i][j] + state;
          }
        }
      }

      return sumArray(grid.map((x) => sumArray(x)));
    }

    const parsedInput = readInput(input);
    return [partOne(parsedInput), partTwo(parsedInput)];
  }

  /**
   * Day 7: Some Assembly Required
   * @param input {string} - The input string.
   * @returns {[number, number]} - [Part One, Part Two] solution.
   */
  day7 = (input: string): number[] => {
    const readInput = (input: string): string[][] => {
      return input.split("\n").map((x) => x.split(" -> ").reverse())
    }

    const unsigned = (n: number): number => { return n % (1 << 16); }

    const evaluate = (a: number, op: string, b: number): number => {
      let ans: number = NaN;
      switch (op) {
        case "NOT":
          ans = unsigned(~a);
          break;
        case "AND":
          ans = unsigned(a & b);
          break;
        case "OR":
          ans = unsigned(a | b);
          break;
        case "LSHIFT":
          ans = unsigned(a << b);
          break;
        case "RSHIFT":
          ans = unsigned(a >> b);
          break;
        default:
          ans = unsigned(a);
      }
      return ans;
    }

    const replaceSignal = (rows: string[][], signal: string, value: number): void => {
      for (let i = 0; i < rows.length; i++) {
        const [sig, ins] = rows[i];
        if (signal === sig) rows[i] = [sig, `${value}`];
      }
    }

    const partOneTwo = (rows: string[][]): Map<string, number> => {

      let signals: Map<string, number> = new Map();
      let i = 0;
      while (rows.length > 0) {
        const [sig, ins]: string[] = rows[i];
        let instruction = ins.split(" ").map((x) => x.trim());
        const n = instruction.length;

        let a: string = "";
        let op: string = "";
        let b: string = "";

        let aVal: number = NaN;
        let bVal: number = NaN;

        switch (n) {
          case 1:
            a = instruction[0];

            if (isDecimal(a)) aVal = Number(a); else aVal = signals.get(a) ?? NaN;

            if (!isNaN(aVal)) {
              signals.set(sig, evaluate(aVal, "", 0));
              rows.splice(i, 1);
              i = -1;
            }
            break;

          case 2:
            [op, a] = instruction;
            if (isDecimal(a)) aVal = Number(a); else aVal = signals.get(a) ?? NaN;
            if (!isNaN(aVal)) {
              signals.set(sig, evaluate(aVal, op, 0));
              rows.splice(i, 1);
              i = -1;
            }
            break;

          default:
            [a, op, b] = instruction;
            if (isDecimal(a)) aVal = Number(a); else aVal = signals.get(a) ?? NaN;
            if (isDecimal(b)) bVal = Number(b); else bVal = signals.get(b) ?? NaN;

            if (!isNaN(aVal) && !isNaN(bVal)) {
              signals.set(sig, evaluate(aVal, op, bVal));
              rows.splice(i, 1);
              i = -1;
            }
        }
        i++;
      }
      return signals;
    }

    let parsedInput: string[][] = readInput(input);
    const ans1: number = partOneTwo(parsedInput).get("a") ?? NaN;

    parsedInput = readInput(input);
    replaceSignal(parsedInput, "b", ans1);
    const ans2: number = partOneTwo(parsedInput).get("a") ?? NaN;

    return [ans1, ans2];
  }

  /**
   * Day 8: Matchsticks
   * @param input {string} - The input string.
   * @returns {[number, number]} - [Part One, Part Two] solution.
   */
  day8 = (input: string): number[] => {
    const partOne = (parsedInput: string[]): number => {

      let slCount: number = 0;
      let memCount: number = 0;

      for (const row of parsedInput) {
        slCount += row.length;

        const decoded = eval(`${row}`);
        memCount += decoded.length;
      }

      return slCount - memCount;
    }

    const partTwo = (parsedInput: string[]): number => {

      let slCount: number = 0;
      let encCount: number = 0;

      for (const row of parsedInput) {
        slCount += row.length;

        let encoded: string = JSON.stringify(row);
        encCount += encoded.length;
      }

      return encCount - slCount;
    }

    const parsedInput: string[] = input.split("\n");
    const ans1: number = partOne(parsedInput);
    const ans2: number = partTwo(parsedInput);

    return [ans1, ans2];
  }

  /**
   * Day 9: All in a Single Night
   * @param input {string} - The input string.
   * @returns {[number, number]} - [Part One, Part Two] solution.
   */
  day9 = (input: string): number[] => {
    interface WeightMap {
      [city: string]: {
        [city: string]: number;
      };
    }

    const readInput = (input: string): [Set<string>, WeightMap] => {
      let cities: Set<string> = new Set<string>();
      let weights: WeightMap = {};

      const lines: string[] = input.split("\n").map((x) => x.replace(" ", ""));

      for (const line of lines) {
        const [C, w] = line.split("=");
        let [ca, cb] = C.split("to");

        ca = ca.trim();
        cb = cb.trim();

        cities.add(ca);
        cities.add(cb);

        if (!weights[ca]) weights[ca] = {};
        weights[ca][cb] = Number(w);

        if (!weights[cb]) weights[cb] = {};
        weights[cb][ca] = Number(w);
      }

      return [cities, weights]
    }

    const partOneTwo = (parsedInput: [Set<string>, WeightMap]): number[] => {
      const [cities, weights] = parsedInput;

      const citiesArr = Array.from(cities);
      const possiblePaths = getPermutations(citiesArr, citiesArr.length);

      let distances: number[] = [];

      for (const path of possiblePaths) {
        let d = 0;
        let i = 0;

        for (let j = 1; j < path.length; j++) {
          d += weights[path[i]][path[j]];
          i += 1;
        }

        distances.push(d)
      }

      return [Math.min(...distances), Math.max(...distances)];
    }

    const parsedInput = readInput(input);
    return partOneTwo(parsedInput);
  }

  /**
   * Day 10: Elves Look, Elves Say
   * @param input {string} - The input string.
   * @returns {number[]} - [Part One, Part Two] solution.
   */
  day10 = (input: string): number[] => {
    const step = (input: string): string => {
      let last: string = input.charAt(0);
      let count: number = 1;
      let output: string[] = [];

      for (let i = 1; i < input.length; i++) {
        const currentChar = input.charAt(i);

        if (currentChar === last) {
          count++;
        } else {
          output.push(`${count}${last}`);
          last = currentChar;
          count = 1;
        }
      }
      output.push(`${count}${last}`);
      return output.join('');
    }

    const partOneTwo = (input: string, times: number): number => {
      let output: string = input;

      for (let i = 0; i < times; i++) {
        output = step(output);
      }
      return output.length;
    }

    return [partOneTwo(input, 40), partOneTwo(input, 50)];
  }
}
