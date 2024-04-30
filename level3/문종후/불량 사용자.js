// function solution(user_id, banned_id) {

//   let types = [];

//   for (let i = 0; i < banned_id.length; i++) {

//     let 기준 = banned_id[i];

//     let type = 0;

//     for (let j = 0; j < user_id.length; j++) {

//       type += comparestring(user_id[j], 기준);

//     }

//     types.push(type);

//   }

//   return types;

// }

// function comparestring(string1, string2) {

//   if (string1.length !== string2.length) {

//     return 0;

//   }

//   let n = string1.length;

//   let flag = true;

//   for (let i = 0; i < n; i++) {

//     if (string1[i] !== string2[i] && string2[i] !== "*") {

//       flag = false;

//     }

//   }

//   return flag ? 1 : 0;

// }

// console.log(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]));

function solution(user_id, banned_id) {
  let answer = 0;
  let visited = [];
  let set = new Set();
  function DFS(x, v, string) {}
}

function comparestring(string1, string2) {
  if (string1.length !== string2.length) return false;
  for (let i = 0; i < string1.length; i++) {
    if (string1[i] !== "*" && string1[i] !== string2[i]) {
      return false;
    }
  }
  return true;
}
