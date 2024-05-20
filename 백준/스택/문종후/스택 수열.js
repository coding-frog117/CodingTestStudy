const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim().split("\n").map(Number);
let n = input.shift();
let stack = [];
let idx = 0;
let str = "";
for (let i = 1; i <= n; i++) {
  stack.push(i);
  str += "+" + "\n";
  while (stack[stack.length - 1] === input[idx]) {
    stack.pop();
    str += "-" + "\n";
    idx++;
    if (idx === n) break;
  }
}
stack.length ? console.log("NO") : console.log(str);
