function solution(storey) {
  let numberstring = storey.toString();
  let n = numberstring.length;
  let first = Number(numberstring[0]);
  let temp = 10 ** (n - 1);
  let case1 = Math.abs(storey - first * temp);
  let case2 = Math.abs(storey - (first + 1) * temp);
  if (case1 > case2) {
  }

  return 10 ** (n - 1);
}

console.log(solution(16));
console.log(solution(2554));

// 6, 4

// 554 446

//재귀
