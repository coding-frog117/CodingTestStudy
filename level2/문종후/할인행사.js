function solution(want, number, discount) {
  let answer = 0;
  let n = discount.length;
  let l = want.length;

  //10일기준으로 원하는 수량과 할인수량이 일치해야함
  //가능한 시작점 기준으로 10일씩 discount 배열을 잘라줌
  for (let i = 0; i < n - 9; i++) {
    const tenday = discount.slice(i, i + 10);

    // 만약 10일단위로 잘린 배열 tenday 동안 구매가능한 품목의 개수와 원하는개수가 일치하지않으면 불가능하다.
    let flag = true;
    for (let j = 0; j < l; j++) {
      if (tenday.filter((item) => item === want[j]).length !== number[j]) {
        flag = false;
        break;
      }
    }
    //가능한경우에는 경우의수를 더해준다.
    if (flag) answer++;
  }
  return answer;
}
