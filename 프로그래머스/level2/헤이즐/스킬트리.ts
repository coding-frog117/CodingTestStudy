/*
https://school.programmers.co.kr/learn/courses/30/lessons/49993

1. 문제분석
1~26자 대문자 문자열 skill, 유니크 -> 순서 보장되어야 함, 중간에 넣기는 가능, 후행 누락은 가능
-> 길이 1~20, 2~26자 skill_trees[], 유니크 -> 이 중 가능한 skill의 수를 리턴
20 * 26 * 26 -> 이거를 n^2 해도 충분하다

2. 풀어보기
'CBD'
'BACDE' -> BCD -> 불가
'CBADF' -> CBD -> 가능
'AECB' -> CB -> 가능
'BDA' -> BD -> 불가

3. 슈도코드
skill이 아예 없어도 관계 없을 것 같고.. -> 각 skills 간의 연관관계는 없어
만약 있다면 -> 후행이 먼저 나오는 케이스만 찾으면 돼. -> 각 인덱스를 구하면? -> 불필요한 연산..
min=0 -> skill_trees[]를 돌려서 -> skill의 indexOf를 걸고 -> min값을 엎어치면서 -> 더 크면 0 리턴
-> 다 돌면 1 리턴 -> 모아서 카운트 해서 result 리턴
*/
{
  const solution = (skill: string, skill_trees: string[]): number => {
    return skill_trees.filter((skill_tree) => {
      let min_index = 0;

      for (const st of skill_tree) {
        let index = skill.indexOf(st);

        if (min_index < index) {
          return false;
        }

        if (index !== -1) {
          min_index++;
        }
      }

      return true;
    }).length;
  };

  console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]));
}
