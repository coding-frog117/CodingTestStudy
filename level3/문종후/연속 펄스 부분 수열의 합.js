function solution(sequence) {
  const n = sequence.length;
  const firstminus = [];
  const firstplus = [];
  let answer = 0;
  for (let i = 0; i < sequence.length; i++) {
    if (i === 0) {
      firstminus.push(-sequence[i]);
      firstplus.push(sequence[i]);
      answer = Math.max(answer, -sequence[i], sequence[i]);
      continue;
    }
    if (i % 2 === 0) {
      firstminus.push(Math.max(firstminus[i - 1] - sequence[i], -sequence[i]));
      firstplus.push(Math.max(firstplus[i - 1] + sequence[i], sequence[i]));
    } else {
      firstminus.push(Math.max(firstminus[i - 1] + sequence[i], sequence[i]));
      firstplus.push(Math.max(firstplus[i - 1] - sequence[i], -sequence[i]));
    }
    answer = Math.max(answer, firstminus[i], firstplus[i]);
  }
  return answer;
}

console.log(solution([2, 3, -6, 1, 3, -1, 2, 4]));
