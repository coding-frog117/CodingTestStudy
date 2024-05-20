// 체크해야하는것이 두가지입니다.
// 1. 끝말잇기 규칙에서 어긋나는가(시작단어가 이전단어에 끝글자와 동일한가?)
// 2. 동일한 단어가나왔는가

// 탈락하는사람의 번호와, 자신이 몇번째차례에서 탈락하는지 구하는법
// 1. 잘못된단어의 인덱스가 주어질떄
//     - 번호는 해당 인덱스 % 인원수
//     - 몇번째는 (해당인덱스 / 인원수) +1
function solution(n, words) {
  var answer = [];
  let temp = words[0];
  if (temp.length === 1) {
    return [1, 1];
  }
  let hash = new Map();
  let index = false;
  hash.set(temp, 1);
  for (let i = 1; i < words.length; i++) {
    let l = temp.length;
    let lastword = temp[l - 1];
    if (words[i].length === 1) {
      index = i;
    }
    if (lastword == words[i][0]) {
      if (hash.has(words[i])) {
        index = i;
      } else {
        hash.set(words[i], 1);
      }
    } else {
      index = i;
    }
    temp = words[i];
  }
  if (index === false) {
    return [0, 0];
  }
  let number = (index % n) + 1;
  let time = Math.floor(index / n) + 1;
  answer.push(number, time);

  return answer;
}

console.log(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]));
