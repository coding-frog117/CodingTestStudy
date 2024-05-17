function solution(fees, records) {
  var answer = [];
  let newrecord = records.map((record) => record.split(" "));
  let timeinfo = new Map();
  let map = new Map();
  for (let i = 0; i < newrecord.length; i++) {
    let times = newrecord[i][0].split(":");
    let time = Number(times[0] * 60) + Number(times[1]);
    let carnumber = newrecord[i][1];
    let type = newrecord[i][2];

    if (type === "IN") {
      map.set(carnumber, time);
      if (!timeinfo.has(carnumber)) {
        timeinfo.set(carnumber, 0);
      }
    } else if (type === "OUT") {
      let spendtime = time - map.get(carnumber);
      map.delete(carnumber);
      timeinfo.set(carnumber, timeinfo.get(carnumber) + spendtime);
    }
  }

  if (map.size) {
    for (let key of map.keys()) {
      let spendtime = 1439 - map.get(key);
      timeinfo.set(key, timeinfo.get(key) + spendtime);
    }
  }
  let moneyinfo = [];

  for (let time of timeinfo.keys()) {
    if (Number(timeinfo.get(time)) < fees[0]) {
      moneyinfo.push([time, fees[1]]);
    } else {
      let money = fees[1] + Math.ceil((timeinfo.get(time) - fees[0]) / fees[2]) * fees[3];
      moneyinfo.push([time, money]);
    }
  }

  moneyinfo
    .sort((a, b) => {
      return Number(a[0]) - Number(b[0]);
    })
    .forEach((money) => answer.push(money[1]));

  return answer;
}

console.log(
  solution(
    [180, 5000, 10, 600],
    [
      "05:34 5961 IN",
      "06:00 0000 IN",
      "06:34 0000 OUT",
      "07:59 5961 OUT",
      "07:59 0148 IN",
      "18:59 0000 IN",
      "19:09 0148 OUT",
      "22:59 5961 IN",
      "23:00 5961 OUT",
    ]
  )
);
