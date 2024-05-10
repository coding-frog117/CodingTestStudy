/*
테스트 1,2,3,6,12만 통과하고 나머지 실패 ■■■■■
https://school.programmers.co.kr/learn/courses/30/lessons/67259

1. 문제분석
3x3 ~ 25x25 정사각형 부지 -> 도면 board -> 0(길) 또는 1(벽) -> 출발점 (0,0) -> 도착점 (N-1,N-1)
상하좌우 === 직선도로, 직선도로의 직각지점 === 코너
-> 직선도로는 100원, 코너 발생시 500원 추가 -> 최소비용 필요
-> 직선도로는 노드수-1 인 것 같고.. 코너는 꺾이는 지점을 체크해야 할 듯?
-> 상하좌우 탐색시, 꺾이면 가중치 추가 -> 탐색시 +100, 꺾이면 +500 추가
너비우선 -> 가중치가 있어서, 먼저 도착하는 게 답이 아닐 수 있어..

2. 풀어보기
문제 설명으로 갈음

3. 슈도코드
상하좌우
*/

const DIRECTION: [0 | 1 | -1, 0 | 1 | -1][] = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];
type Direction = "W" | "H" | "";
type Count = number;
const solution = (maps: number[][]): number => {
  const queue: [number, number, Direction, Count][] = [[0, 0, "", 0]];
  let first = 0;
  maps[0][0] = 1;

  while (first < queue.length) {
    const [x, y, direction, sum] = queue[first++];
    if (x === maps.length - 1 && y === maps[0].length - 1) {
      return sum;
    }

    const moves: [number, number, Direction][] = [];
    for (const [_x, _y] of DIRECTION) {
      if (maps[x + _x]?.[y + _y] === 0) {
        const move_x = x + _x;
        const move_y = y + _y;
        const move_direction = _x === 0 ? "H" : _y === 0 ? "W" : "";
        moves.push([move_x, move_y, move_direction]);
      }
    }

    const straights = moves.filter(
      (move) => direction === move[2] || direction === ""
    );
    if (straights.length) {
      straights.forEach(([move_x, move_y, move_direction]) => {
        maps[move_x][move_y] = 1;
        queue.push([move_x, move_y, move_direction, sum + 100]);
      });
    } else {
      moves.forEach(([move_x, move_y, move_direction]) => {
        maps[move_x][move_y] = 1;
        queue.push([move_x, move_y, move_direction, sum + 600]);
      });
    }
  }

  return -1;
};

console.log(
  solution([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
  ])
);
console.log(
  solution([
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
  ])
);
console.log(
  solution([
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 0],
  ])
);
console.log(
  solution([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
  ])
);
