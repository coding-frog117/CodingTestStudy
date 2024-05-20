// function solution(topping) {
//   let answer = 0;
//   for (let i = 1; i < topping.length; i++) {
//     let first = new Set(topping.slice(0, i));
//     let second = new Set(topping.slice(i));
//     if (first.size === second.size) {
//       answer++;
//     }
//   }
//   return answer;
// }

//시간초과,
//풀이변경..종류를 뺴주는식으로

function solution(topping) {
  const hash = new Map();
  const first = new Set();
  let answer = 0;
  for (let i = 0; i < topping.length; i++) {
    if (hash.has(topping[i])) {
      hash.set(topping[i], hash.get(topping[i]) + 1);
    } else {
      hash.set(topping[i], 1);
    }
  }
  for (let i = 0; i < topping.length; i++) {
    let rest = hash.get(topping[i]) - 1;
    first.add(topping[i]);
    if (rest > 0) {
      hash.set(topping[i], rest);
    } else {
      hash.delete(topping[i]);
    }
    if (first.size === hash.size) answer++;
  }

  return answer;
}

console.log(solution([1, 2, 1, 3, 1, 4, 1, 2]));
console.log(solution([1, 2, 3, 1, 4]));
