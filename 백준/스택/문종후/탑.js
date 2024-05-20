const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim().split("\n");
let N = Number(input.shift());
let heights = input.join(" ").split(" ").map(Number);
let stack = [];
let answer = [];

for (let i = 0; i < N; i++) {
  while (stack.length && heights[stack[stack.length - 1]] < heights[i]) {
    stack.pop();
  }
  if (stack.length) {
    answer[i] = stack[stack.length - 1] + 1;
  }
  stack.push(i);
}
console.log(answer.join(" "));

// while (stack.length) {
//   let laser = stack.pop();

//   let flag = false;
//   for (let i = stack.length - 1; i >= 0; i--) {
//     if (stack[i] >= laser) {
//       answer.push(i + 1);
//       flag = true;
//       break;
//     }
//   }
//   if (!flag) {
//     answer.push(0);
//   }
// }
// answer = answer.reverse().join(" ");
// console.log(answer);
