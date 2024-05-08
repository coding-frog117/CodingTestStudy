/* 
https://school.programmers.co.kr/learn/courses/30/lessons/42579

1. 문제분석
베스트 집계로직 -> 장르 재생수 큰 순 -> 장르내 재생수 큰 순 -> 인덱스 작은 순 -> 장르내 최대 2개만
사실상 genres와 plays는 같은 데이터 -> 일단 합치고 생각 -> 베스트 집계된 인덱스 순서대로 리턴
입력 개수는 1~10000, 장르 종류는 100개 미만 -> n^2을 돌려도 관계없긴 함
일단 모든 장르는 들어간다. 재생수가 적다고 빠지는 장르는 없음. 빠지는 건 장르별 인덱스임.

2. 풀어보기
['classic','pop','classic','classic','pop']
[500,600,150,800,2500]
{classic -> 1450, pop -> 3100} -> [4,1,3,0]

3. 슈도코드
genres[]와 plays[]를 묶어 total_play_by_genre {} 만듦 -> Array.from으로 genre_by_play[] 만들고 정렬
plays_by_genre {} 만듦 -> 장르내 재생수는 여기로 집계 -> [인덱스, 재생수][]
 -> 장르내 정렬(재생수, 인덱스)하고 length 2로 자름 -> 안정정렬이니 인덱스 작은 순은 알아서 된다
genre_by_play[] 리딩으로 plays_by_genre[] 조인해서 result[] 리턴.
*/

const by_desc = (a: [unknown, number], b: [unknown, number]) => b[1] - a[1];
const solution = (genres: string[], plays: number[]): number[] => {
  if (genres.length === 0 && plays.length === 0) {
    return [];
  }

  const total_play_by_genre = new Map<string, number>();
  const plays_by_genre = new Map<string, [number, number][]>();

  for (let i = 0; i < genres.length; i++) { // genres.length === plays.length
    const genre = genres[i];
    const play = plays[i];

    total_play_by_genre.set(genre, (total_play_by_genre.get(genre) ?? 0) + play);

    const plays_in_genre = plays_by_genre.get(genre) ?? [];
    plays_in_genre.push([i, play]);
    plays_by_genre.set(genre, plays_in_genre);
  }

  return Array.from(total_play_by_genre).sort(by_desc).flatMap(([genre]) => {
    const plays_in_genre = plays_by_genre.get(genre) ?? [];
    plays_in_genre.sort(by_desc);
    plays_in_genre.length = 2;
    return plays_in_genre.map(([index]) => index);
  });
}

console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]));