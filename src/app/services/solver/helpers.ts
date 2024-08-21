/**
 * Gets the combinations of an array.
 * @param {T} arr - The array to get the combinations from.
 * @param {number} size - The size of the combinations.
 * @returns {T[][]} - The combinations of the array.
 */
export function getCombinations<T>(arr: T[], size: number): T[][] {
  if (size > arr.length || size <= 0) {
    return [];
  }

  if (size === arr.length) {
    return [arr];
  }

  if (size === 1) {
    return arr.map(element => [element]);
  }

  const combinations: T[][] = [];

  for (let i = 0; i <= arr.length - size; i++) {
    const head = arr.slice(i, i + 1);
    const tailCombinations = getCombinations(arr.slice(i + 1), size - 1);
    for (const tail of tailCombinations) {
      combinations.push(head.concat(tail));
    }
  }

  return combinations;
}

/**
 * Gets the permutations of an array.
 * @param {T} arr - The array to get the combinations from.
 * @param {number} size - The size of the combinations.
 * @returns {T[][]} - The combinations of the array.
 */
export function getPermutations<T>(arr: T[], size: number): T[][] {
  const results: T[][] = [];

  function permute(current: T[], remaining: T[]): void {
    if (current.length === size) {
      results.push([...current]);
      return;
    }

    for (let i = 0; i < remaining.length; i++) {
      const newCurrent = current.concat(remaining[i]);
      const newRemaining = remaining.slice(0, i).concat(remaining.slice(i + 1));
      permute(newCurrent, newRemaining);
    }
  }

  permute([], arr);
  return results;
}

/**
 * Adds two arrays.
 * @param {number[]} arrA - The first array.
 * @param {number[]} arrB - The second array. 
 * @returns {number[]} - The sum of the two arrays.
 */
export function addArrs(arrA: number[], arrB: number[]): number[] {
  let response = [];
  for (let i: number = 0; i < arrA.length; i++) {
    response.push(arrA[i] + arrB[i]);
  }
  return response;
}

/**
 * Compares two arrays.
 * @param {any[]} arrayA - The first array.
 * @param {any[]} arrayB - The second array.
 * @returns {boolean} - True if the arrays are equal, false otherwise.
 */
export function arraysEqual(arrayA: any[], arrayB: any[]): boolean {
  if (arrayA.length !== arrayB.length) return false;
  for (let i = 0; i < arrayA.length; i++) {
    if (arrayA[i] !== arrayB[i]) return false;
  }
  return true;
}

/**
 * Checks if an array contains another array.
 * @param {any[][]} source - The source array.
 * @param {any[]} target - The target array.
 * @returns {boolean} - True if the source array contains the target array, false otherwise.
 */
export function containsArray(source: any[][], target: any[]): boolean {
  for (const array of source) {
    if (arraysEqual(array, target)) {
      return true;
    }
  }
  return false;
}

/**
 * Gets the sum of an array.
 * @param {number[]} arr - The array to sum.
 * @returns {number} - The sum of the array.
 */
export const sumArray = (arr: number[]): number => arr.reduce((a, b) => a + b, 0);

/**
 * Evaluate if a value is a decimal.
 * @param {string | number} value - The value to evaluate.
 * @returns {boolean} - True if the value is a decimal, false otherwise.
 */
export function isDecimal(value?: string | number): boolean {
  return ((value != null) &&
    (value !== '') &&
    !isNaN(Number(value.toString())));
}
