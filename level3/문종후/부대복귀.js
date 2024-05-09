//최단시간에 부대복귀

function solution(n, roads, sources, destination) {
  var answer = [];
  const graph = new Array(n + 1).fill(0).map((_) => []);
  roads.forEach(([from, to]) => {
    graph[from].push(to);
    graph[to].push(from);
  });

  return answer;
}

console.log(
  solution(
    3,
    [
      [1, 2],
      [2, 3],
    ],
    [2, 3],
    1
  )
);
