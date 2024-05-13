//DFS 문제?
function solution(tickets) {
  tickets.sort();
  let n = tickets.length;
  let visited = Array.from({ length: n }, () => false);
  let answer = [];
  function DFS(cur, cnt, path) {
    if (cnt === tickets.length && answer.length === 0) {
      answer = path;
      return;
    }
    for (let i = 0; i < tickets.length; i++) {
      if (visited[i]) continue;
      if (tickets[i][0] === cur) {
        visited[i] = true;
        DFS(tickets[i][1], cnt + 1, [...path, tickets[i][1]]);
      }
    }
  }
  DFS("ICN", 0, ["ICN"]);
  return answer;
}
console.log(
  solution([
    ["ICN", "JFK"],
    ["HND", "IAD"],
    ["JFK", "HND"],
  ])
);
console.log(
  solution([
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
  ])
);
