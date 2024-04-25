function solution(A, B) {
  let answer = 0;
  let n = A.length;

  //크기가 큰순서대로 정렬
  A.sort((a, b) => b - a);
  B.sort((a, b) => b - a);
  // B 인덱스
  let j = 0;
  for (let i = 0; i < n; i++) {
    //배열에서 가장큰수끼리비교
    // 만약 B가더크다면 이겻으니 1승추가,다음사람으로 바꿔줌.
    if (A[i] < B[j]) {
      answer++;
      j++;
    }
  }
  return answer;
}

console.log(solution([5, 1, 3, 7], [2, 2, 6, 8]));
