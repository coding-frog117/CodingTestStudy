// weights 배열에서 두쌍을 모두구한다.(초과)
// 두쌍의 최대공약수로 나눠준다.
// 두쌍의값이 arr에 포함된다면 균형을 이루는것이다.

// 기준점을 하나잡고 비율을 곱해준다.
// 큰수기준으로할시 1 , 3/2, 2 ,4/3
// 작은수 기준 1, 2/3,1/2,3/4
function solution(weights) {
  let answer = 0;
  const map = new Map();
  let rating = [1, 3 / 2, 2, 4 / 3];

  weights.sort((a, b) => b - a);
  console.log(weights);

  for (let i = 0; i < weights.length; i++) {
    for (let j = 0; j < rating.length; j++) {
      if (map.has(weights[i] * rating[j])) {
        answer += map.get(weights[i] * rating[j]);
      }
    }
    map.set(weights[i], (map.has(weights[i]) ? map.get(weights[i]) : 0) + 1);
  }
  console.log(map);
  return answer;
}

console.log(solution([100, 180, 360, 100, 270]));
