const fs = require("fs");
const input = fs.readFileSync("example.txt").toString();
let stack = [];
let answer = 0;
let n = input.length;
for (let i = 0; i < n; i++) {
  if (input[i] === "(") {
    stack.push(input[i]);
  } else {
    stack.pop();
    if (input[i - 1] == "(") {
      answer += stack.length;
    } else {
      answer++;
    }
  }
}

console.log(answer);
