function solution(genres, plays) {
  let hash = new Map();
  //장르와 노래의 인덱스를 저장
  for (let i = 0; i < genres.length; i++) {
    //장르가 O->장르 노래목록에 추가.
    if (hash.has(genres[i])) {
      hash.set(genres[i], [...hash.get(genres[i]), [i, plays[i]]]);
    } else {
      hash.set(genres[i], [[i, plays[i]]]);
    }
  }
  //장르별 재생횟수
  let total = [];
  for (const x of hash) {
    let key = x[0];
    let song = x[1].length;
    let sum = 0;
    for (let i = 0; i < song; i++) {
      sum += x[1][i][1];
    }
    //[장르이름,재생횟수]
    total.push([key, sum]);
  }
  let answer = [];
  //재생횟수에따라 내림차순정렬
  total.sort((a, b) => b[1] - a[1]);

  for (let i = 0; i < total.length; i++) {
    //해당장르노래가 2개이상이면, 재생횟수에따라 내림차순정렬 후 2개선정
    if (hash.get(total[i][0]).length >= 2) {
      let max = hash.get(total[i][0]).sort((a, b) => b[1] - a[1]);
      answer.push(max[0][0]);
      answer.push(max[1][0]);
      //노래가 한개이면 해당노래를 asnwer 에추가
    } else answer.push(hash.get(total[i][0])[0][0]);
  }
  return answer;
}
