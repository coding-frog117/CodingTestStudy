/*
https://school.programmers.co.kr/learn/courses/30/lessons/131704

1. 문제분석
스택 -> order[]와 길이가 같고 1부터 n까지인 box[] -> 가능한 최대 개수 리턴

2. 풀어보기
[4,3,1,2,5] -> stack [1,2,3] -> [4] -> stack [1,2], [4,3] -> 2
[5,4,3,2,1] -> stack [1,2,3,4] -> [5,4,3,2,1] -> 5

3. 슈도코드
order[] -> stack[] 만들고 -> 1부터 돌려서 -> order.first가 아니면 stack에 push
-> order.first이면 first++ -> stack.top이면 stack에서 pop, first++ 반복 -> length - first 리턴
*/
{
  const solution = (order: number[]): number => {
    const stack: number[] = [];
    let first = 0;
    for (let number = 1; number <= order.length; number++) {
      if (number === order[first]) {
        first++;
      } else {
        stack.push(number);
      }
      while (first < order.length && order[first] === stack[stack.length - 1]) {
        first++;
        stack.pop();
      }
    }

    return first;
  };

  console.log(solution([4, 3, 1, 2, 5]));
  console.log(solution([5, 4, 3, 2, 1]));
}
