//y가제일크면 root, 작으면 쫄따구
//각 root 기준 x가 작으면 왼쪽 x가 크면 오른쪽
//y크기순으로정렬, y가 같으면 x를 오름차순정렬하자.
//nodeinfo 에 공번호를 넣어주자.
//root가 바뀌니까 재귀형태로구현 dfs?

function solution(nodeinfo) {
  var answer = [[]];
  for (let i = 0; i < nodeinfo.length; i++) {
    nodeinfo[i].push(i + 1);
  }
  nodeinfo.sort((a, b) => {
    if (a[1] === b[1]) {
      return a[0] - b[0];
    } else {
      return b[1] - a[1];
    }
  });
  let pre = [];
  let post = [];
  function dfs(info, preorder) {
    if (info.length === 0) {
      return;
    }
    let current = 0;
    let left = [];
    let right = [];
    preorder.push(info[current][2]);
    for (let i = 1; i < info.length; i++) {
      if (info[i][0] < info[current][0]) {
        left.push(info[i]);
      } else {
        right.push(info[i]);
      }
    }
    dfs(left, preorder);
    dfs(right, preorder);
  }

  dfs(nodeinfo, pre);
  console.log(pre);
  //   console.log(pre, post);
}

console.log(
  solution([
    [5, 3],
    [11, 5],
    [13, 3],
    [3, 5],
    [6, 1],
    [1, 3],
    [8, 6],
    [7, 2],
    [2, 2],
  ])
);
