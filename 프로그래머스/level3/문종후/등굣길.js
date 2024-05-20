function solution(m, n, puddles) {
  // m이 가로의 길이, n이 세로의 길이.
  const map = Array.from({ length: n }).map((v) => Array.from({ length: m }).fill(1));

  // 물 웅덩이는 0으로 센다.
  puddles.forEach(([m, n]) => {
    map[n - 1][m - 1] = 0;
  });

  // 해당 칸의 값이 0이라면 물 웅덩이를 지나는 경로이므로 값을 0으로 설정
  // 첫 행 첫 열일 경우 값을 1로 초기화
  // 이 외의 첫 행일 경우 왼쪽만
  // 첫 열일 경우 위에서오는경우만
  // 나머지는 위에서 오는 경로의 개수와 왼쪽에서 오는 경로의 개수를 더해준다.
  const result = [];

  for (let i = 0; i < n; i++) {
    result.push([]);
    for (let j = 0; j < m; j++) {
      if (i === 0 && j === 0) {
        result[i][j] = 1;
      } else if (map[i][j] === 0) {
        result[i][j] = 0;
      } else if (i === 0) {
        result[i][j] = result[i][j - 1];
      } else if (j === 0) {
        result[i][j] = result[i - 1][j];
      } else {
        result[i][j] = result[i - 1][j] + result[i][j - 1];
      }
    }
  }

  return result[n - 1][m - 1];
}

console.log(solution(4, 3, [[2, 2]]));
