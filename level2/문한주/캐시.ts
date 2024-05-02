/* 
https://school.programmers.co.kr/learn/courses/30/lessons/17680

1. 문제분석
정수 30개 cacheSize -> 도시이름 20자 10만개 queris -> 공백.숫자.특수문자 없음,대소문자 구분 X
-> hit시 실행시간 1, miss시 실행시간 5 -> 실행시간 다 더해서 리턴
당연히 쿼리는 순서대로 들어오는 걸 가정하는 거겠지? 그냥 맵 써서 타임스탬프를 넣을까?

2. 풀어보기
2	-> ['Jeju','Pangyo','NewYork','newyork'] -> 일단 miss 3개 15 + hit 1개 1 -> 16
3	-> ['Jeju','Pangyo','Seoul','NewYork','LA','Jeju','Pangyo','Seoul','NewYork','LA']
 -> miss 5개 -> 연달아 expired 되서 miss 5개 -> 50
3	-> ['Jeju','Pangyo','Seoul','Jeju','Pangyo','Seoul','Jeju','Pangyo','Seoul']
-> miss 3개 -> hit 3개 -> hit 3개 -> 21
5	-> ['Jeju','Pangyo','Seoul','NewYork','LA','SanFrancisco','Seoul','Rome','Paris','Jeju','NewYork','Rome']	52
0	-> ['Jeju','Pangyo','Seoul','NewYork','LA']	-> miss 5개 -> 25

3. 슈도코드
cache[] size가 최대 30이니 크지 않아. 앞에다 넣고, length를 계속 쳐서 날린다
-> 30*10만 -> 300만 -> 실행가능.
cacheSize, cities[] -> cache[]에서 indexOf -> -1이면 5, 아니면 1 + splice
-> 0번 인덱스에 splice로 삽입 -> cache.length = cacheSize로 날림
+ 계속 lowerCase를 쳐준다
*/

const solution = (cache_size: number, cities: string[]) => {
  if (cache_size === 0) {
    return cities.length * 5;
  }
  const cache: string[] = [];
  let total_time = 0;
  for (const city of cities) {
    const query = city.toLowerCase();
    const i = cache.indexOf(query);
    if (i === -1) {
      total_time += 5;
    } else {
      total_time += 1;
      cache.splice(i, 1);
    }
    cache.splice(0, 0, query);
    cache.length = cache_size;
  }
  return total_time;
}
console.log(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]));
console.log(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]));
console.log(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]));
console.log(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]));
console.log(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]));
console.log(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]));