let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n").map(Number);
let n = input.shift();
let Stack = [];
let answer = 0;
for (let i = 0; i < input.length; i++) {
  while (Stack.length) {
    if (Stack[Stack.length - 1] <= input[i]) {
      Stack.pop();
    } else break;
  }
  Stack.push(input[i]);

  answer += Stack.length - 1;
}

console.log(answer);
