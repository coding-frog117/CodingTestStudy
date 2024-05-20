//풍선중 더 작은 풍선을 터트리는 행위는 한번만 할수있다.
//큰거위주로 터트림. 작은것만남는다.
//이때 마지막으로 남은풍선 두개에따라서 결정되는문제?
//작은 풍선
//완탐불가능.
//이진탐색?
function solution(a) {
  const n = a.length;
  const left = new Array(n);
  const right = new Array(n);
  left[0] = a[0];
  right[n - 1] = a[n - 1];
  for (let i = 1; i < n; i++) {
    left[i] = Math.min(left[i - 1], a[i]);
  }
  for (let i = n - 2; i >= 0; i--) {
    right[i] = Math.min(right[i + 1], a[i]);
  }
  console.log(left, right);
}
console.log(solution([9, -1, -5]));
