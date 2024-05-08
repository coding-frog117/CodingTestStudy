//가장긴 팰린드롬문자열을 찾아야됨
//만약 팰린드롬이 없다면 1을 리턴하면된다.(자기자신)
//자기자신확인하고, 1적은거확인 (앞에거 1짜르냐 뒤에거 1짜르냐)
//2적은거확인(앞에거 2짜르냐, 뒤에거 2짜르냐)

function solution(s) {
  for (let i = s.length; i >= 1; i--) {
    for (let j = 0; j <= s.length - i; j++) {
      const substr = checkPalindrome(s.slice(j, i + j));
      if (substr) return i;
    }
  }
  return 1;
}

function checkPalindrome(string) {
  let reversed = string.split("").reverse().join("");
  return string === reversed;
}
