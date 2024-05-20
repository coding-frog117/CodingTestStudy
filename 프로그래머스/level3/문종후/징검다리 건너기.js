//이문제는 이진탐색으로 범위를 좁히는형식으로 접근이가능합니다.
//왜냐하면, 주어진 배열에서 특정값을 뺐을때 연속되는 0밑의 숫자가 k와 같거나 클경우
//더이상 못건너게되기때문이다.

function solution(stones, k) {
  let answer = 1;
  let right = 200000000;
  while (answer <= right) {
    const mid = Math.floor((answer + right) / 2);
    let count = 0;
    for (const stone of stones) {
      if (stone - mid <= 0) count++;
      else count = 0;
      if (count >= k) break;
    }
    if (count >= k) right = mid - 1;
    else {
      answer = mid + 1;
    }
  }

  return answer;
}

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3));
