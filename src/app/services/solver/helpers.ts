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
