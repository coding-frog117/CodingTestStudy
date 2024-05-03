//DFS 시간초과
//DP?
function solution(land) {
  var answer = 0;
  let n = land.length;
  const dp = new Array(n).fill(0).map(() => new Array(4).fill(0)); // 다이나믹 프로그래밍 테이블 생성

  // 초기값 설정
  for (let i = 0; i < 4; i++) {
    dp[0][i] = land[0][i];
  }
}

console.log(
  solution([
    [1, 2, 3, 5],
    [5, 6, 7, 8],
    [4, 3, 2, 1],
  ])
);
