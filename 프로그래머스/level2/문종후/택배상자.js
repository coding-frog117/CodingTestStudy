function solution(order) {
  //order 의 인덱스를 표현해줍니다. (나간상자의 개수)
  let answer = 0;
  //컨테이너벨트입니다.
  let container = [];
  //order 배열을 탐색
  //컨테이너벨트에 순서대로 숫자를 집어넣다가, 만약 뽑아야하는 녀석과 container 의 맨위가 같다면,
  // 상자가 빠졌기떄문에, 빼주고 인덱스를 1더해준다.
  for (let i = 1; i <= order.length; i++) {
    container.push(i);
    while (container.length !== 0 && container[container.length - 1] === order[answer]) {
      container.pop();
      answer++;
    }
  }
  return answer;
}

console.log(solution([4, 3, 1, 2, 5]));
