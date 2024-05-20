function solution(sequence, k) {
  let answer = [];
  let n = sequence.length;
  let left = 0;
  let sum = 0;
  //투포인터알고리즘
  for (let right = 0; right < n; right++) {
    sum += sequence[right];
    if (sum === k) answer.push([left, right]);
    while (sum >= k) {
      sum -= sequence[left];
      left++;
      if (sum === k) answer.push([left, right]);
    }
  }
  //부분수열의합이 k가되는 인덱스모음 answer을 문제기준에따라정렬
  //1 . 길이가짧은순
  //2 . 길이가 같다면 인덱스가빠른쪽
  answer.sort((a, b) => {
    //인덱스 배열의 차이 == 길이
    const diffA = Math.abs(a[0] - a[1]);
    const diffB = Math.abs(b[0] - b[1]);
    //만약 두길이가 같다면 인덱스가 빠른순으로 정렬
    if (diffA === diffB) {
      return a[0] - b[0];
    }
    //길이가 짧은순으로 정렬
    else {
      return diffA - diffB;
    }
  });
  return answer[0];
}

console.log(solution([1, 1, 1, 2, 3, 4, 5], 5));
