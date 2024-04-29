function solution(n, stations, w) {
  var answer = 0;
  let apart = Array.from({ length: n }, () => false);
  for (let i = 0; i < stations.length; i++) {
    markCovered(apart, stations[i], w);
  }
  for (let i = 0; i < n; ) {
    if (!apart[i]) {
      let install = Math.min(i + w, n);
      markCovered(apart, install, w);
      answer++;
      i = install + w + 1;
    } else {
      i++;
    }
  }

  return answer;
}

function markCovered(apart, station, w) {
  let leftRange = Math.max(station - w, 1); // 왼쪽 범위
  let rightRange = Math.min(station + w, apart.length); // 오른쪽 범위

  for (let i = leftRange; i <= rightRange; i++) {
    apart[i - 1] = true;
  }
}

console.log(solution(11, [4, 11], 1));
console.log(solution(16, [9], 2));
