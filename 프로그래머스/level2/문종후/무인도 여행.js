function solution(maps) {
  let answer = [];
  let map = [];
  let dx = [-1, 1, 0, 0];
  let dy = [0, 0, -1, 1];
  //인접행렬화
  for (let i = 0; i < maps.length; i++) {
    map.push(maps[i].split(""));
  }
  //DFS
  function DFS(x, y) {
    //범위밖이면 0
    if (x < 0 || y < 0 || x >= maps.length || y >= map[0].length || map[x][y] === "X") return 0;
    //현재위치 식량->숫자변경
    let now = Number(map[x][y]);
    //이미방문한곳이라 X로초기화
    map[x][y] = "X";
    //4방향에대해 현재값에서 더해주면 무인도 총생활시간
    for (let k = 0; k < 4; k++) {
      let nx = x + dx[k];
      let ny = y + dy[k];
      now += DFS(nx, ny);
    }
    return now;
  }
  //그래프탐색
  for (let i = 0; i < map.length; i++) {
    for (let j = 0; j < map[0].length; j++) {
      if (map[i][j] !== "X") {
        answer.push(DFS(i, j));
      }
    }
  }
  //섬이없으면 [-1] 출력 있으면 오름차순으로 출력
  return answer.length ? answer.sort((a, b) => a - b) : [-1];
}
