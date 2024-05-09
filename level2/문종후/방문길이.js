//길을 저장해야됨 (중복없이 Set, Map?)
function solution(dirs) {
  let answer = 0;
  const move = {
    U: [-1, 0],
    D: [1, 0],
    R: [0, 1],
    L: [0, -1],
  };
  let visited = new Set();
  let now = [0, 0];
  for (let dir of dirs) {
    let nx = now[0] + move[dir][0];
    let ny = now[1] + move[dir][1];
    //5,-5 범위를 넘어가면 패쓰
    if (nx < -5 || nx > 5 || ny < -5 || ny > 5) continue;
    //양방향을 넣어줘야됨
    visited.add(`${now[0]}${now[1]}${nx}${ny}`);
    visited.add(`${nx}${ny}${now[0]}${now[1]}`);

    now = [nx, ny];
  }
  answer = Math.floor(visited.size / 2);
  return answer;
}

console.log(solution("ULURRDLLU"));
