type index = number;
const RATE: [number, number][] = [
  [1, 1],
  [1, 2],
  [2, 3],
  [3, 4],
  [2, 1],
  [3, 2],
  [4, 3],
];

const solution1 = (weights: number[]): number => {
  let count = 0;

  for (let i = 0; i < weights.length; i++) {
    const matcheds = RATE.map((rate) => (weights[i] * rate[0]) / rate[1])
      .filter(Number.isInteger)
      .map((rw) => weights.filter((weight) => weight === rw).length)
      .reduce((sum, count) => sum + count, 0);
    count += matcheds - 1;
  }

  return count / 2;
};

const solution2 = (weights: number[]): number => {
  let count = 0;
  const map = new Map<number, number>();

  for (let i = 0; i < weights.length; i++) {
    const rates = RATE.map((rate) => (weights[i] * rate[0]) / rate[1]).filter(
      Number.isInteger
    );
    const matcheds = rates
      .map((rate) => map.get(rate) ?? 0)
      .reduce((sum, count) => sum + count, 0);
    count += matcheds;
    map.set(weights[i], (map.get(weights[i]) ?? 0) + 1);
  }

  return count;
};
