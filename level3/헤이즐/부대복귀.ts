/*
테스트 6~16 실패 ■■■■■
https://school.programmers.co.kr/learn/courses/30/lessons/132266

1. 문제분석
지역 -> 번호로 구분됨 -> 지역 간 이동시간은 항상 1
n은 지역의 수, roads[]는 연결된 길, sources[]는 현재 위치, destination은 목표점
-> sources[]별 도착 가능한 최단시간을 result[]로 담아 리턴 -> 불가능하면 -1
-> n 3~10만, roads[] 길이 2~50만 + 중복없음, sources는 1~500

2. 풀어보기
지역 1~3 -> 연결 [[1, 2], [2, 3]] -> 목표 1
-> 시작점 2 -> 2-1 -> 1회
-> 시작점 3 -> 3-2-1 -> 2회
지역 1~5 -> 연결 [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]] -> 목표 5
-> 시작점 1 -> 1-2-5, 1-4-5 -> 2회
-> 시작점 3 -> -1회
-> 시작점 5 -> 0회

3. 슈도코드
최적해를 찾아야 하니 너비우선탐색?
시작점에서 시작 -> 연결점을 찾으면 -> 그걸 시작점으로 재귀 -> 카운트 리턴 -> start
-> 다 모아서 제일 작은 값 적재 -> 시작점 별로 모아서 리턴 -> n은 어디다 쓰지?
*/
{
  type Road = [number, number];
  const cache: [number, number][] = [];
  const countMove = (
    start: number,
    mid: number,
    destination: number,
    roads: Road[],
    count: number
  ): number => {
    if (mid === destination) {
      const hit = cache.find((c) => c[0] === start);
      if (hit) {
        hit[1] = Math.min(hit[1], count);
      } else {
        cache.push([start, count]);
      }
      return count;
    }
    const hit = cache.find((c) => c[0] === mid);
    if (hit) {
      return count + hit[1];
    }

    const result = new Set<number>();
    for (let i = 0; i < roads.length; i++) {
      const [a, b] = roads[i];
      const end = mid === a ? b : mid === b ? a : null;
      if (end) {
        const others = [...roads];
        others.splice(i, 1);
        result.add(countMove(start, end, destination, others, count + 1));
      }
    }

    if (result.size) {
      if (result.has(-1)) {
        if (result.size === 1) {
          return -1;
        } else {
          result.delete(-1);
        }
      }
      const min = Math.min(...result);
      return min;
    }

    return -1;
  };
  const solution = (
    n: number,
    roads: Road[],
    sources: number[],
    destination: number
  ): number[] => {
    return sources.map((source) =>
      countMove(source, source, destination, roads, 0)
    );
  };

  console.log(
    solution(
      3,
      [
        [1, 2],
        [2, 3],
      ],
      [2, 3],
      1
    )
  );
  console.log(
    solution(
      5,
      [
        [1, 2],
        [1, 4],
        [2, 4],
        [2, 5],
        [4, 5],
      ],
      [1, 3, 5],
      5
    )
  );
}
