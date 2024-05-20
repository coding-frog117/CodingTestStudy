function solution(enroll, referral, seller, amount) {
  const members = new Map();
  enroll.forEach((member, i) => {
    members.set(member, { referral: referral[i], profit: 0 });
  });
  seller.forEach((member, i) => {
    let curAmount = amount[i] * 100;
    let curMember = members.get(member);
    while (curAmount && curMember) {
      div = Math.floor(curAmount / 10);
      curMember.profit += curAmount - div;
      curAmount = div;
      curMember = members.get(curMember.referral);
    }
  });
  return enroll.map((member) => members.get(member).profit);
}

//재귀적으로 구현합니다.

console.log(
  solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
  )
);
