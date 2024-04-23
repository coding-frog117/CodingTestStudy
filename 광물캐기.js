function solution(picks, minerals) {
  const pick = picks.reduce((a, b) => a + b, 0);
  let answer = 0;
  minerals = minerals.slice(0, pick * 5);
  let typeMinerals = [];
  for (let idx = 0; idx < minerals.length; idx++) {
    const curr = minerals[idx];
    const index = Math.floor(idx / 5);

    if (!typeMinerals[index]) typeMinerals[index] = [0, 0, 0];

    if (curr === "diamond") {
      typeMinerals[index][0]++;
    } else if (curr === "iron") {
      typeMinerals[index][1]++;
    } else if (curr === "stone") {
      typeMinerals[index][2]++;
    }
  }
  typeMinerals.sort((a, b) => b[0] - a[0] || b[1] - a[1]);
  typeMinerals.forEach((mineral) => {
    const [diamond, iron, stone] = mineral;
    if (picks[0]) {
      answer += diamond + iron + stone;
      picks[0]--;
    } else if (picks[1]) {
      answer += diamond * 5 + iron + stone;
      picks[1]--;
    } else if (picks[2]) {
      answer += diamond * 25 + iron * 5 + stone;
      picks[2]--;
    }
  });
  return answer;
}
