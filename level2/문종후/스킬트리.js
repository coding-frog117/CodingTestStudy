function solution(skill, skill_trees) {
  let count = 0;
  for (skill of skill_trees) {
    let stack = skill.split("");
    let flag = stack[0];
    let answer = true;
    for (let i = 0; i < skill.length; i++) {
      if (skill[i] === flag) {
        stack.shift();
        flag = stack[0];
      } else if (stack.includes(skill[i]) && skill[i] !== flag) {
        answer = false;
      }
    }
    if (answer) count++;
  }
  return count;
}
