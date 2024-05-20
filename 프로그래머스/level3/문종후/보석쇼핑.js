function solution(gems) {
  let answer = [];
  let gemstype = new Set(gems).size;
  let map = new Map();
  gems.forEach((gem, index) => {
    map.delete(gem);
    map.set(gem, index);
    if (map.size === gemstype) {
      answer.push([map.values().next().value + 1, index + 1]);
    }
  });
  answer = answer.sort((a, b) => a[1] - a[0] - (b[1] - b[0]))[0];

  return answer;
}

console.log(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]));
