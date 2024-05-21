let [N, ...input] = require("fs").readFileSync("dev/stdin").toString().trim().split("\n");

function solution(N, input) {
  let arr = input[0].split(" ").map(Number);
  let answer = Array.from({ length: N }, () => -1);
  let stack = [];
  for (let i = 0; i < N; i++) {
    while (stack.length && arr[stack[stack.length - 1]] < arr[i]) {
      answer[stack.pop()] = arr[i];
    }
    stack.push(i);
  }
  return answer.join(" ");
}
console.log(solution(N, input));
