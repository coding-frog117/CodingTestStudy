function solution(cacheSize, cities) {
  var answer = 0;
  let cache = [];
  //캐시 크기가 0인 경우는 전부 캐시미스처리
  if (cacheSize === 0) return cities.length * 5;

  //도시배열이 비어있을떄까지
  while (cities.length) {
    //맨앞도시, 대소문자통일(소문자통일)
    const city = cities.shift().toLowerCase();
    //캐시에 해당도시가 존재하는경우
    if (cache.includes(city)) {
      //해당도시를 캐시에서 제거
      cache.splice(cache.indexOf(city), 1);
      //캐시의 가장최근도시로 추가
      cache.push(city);
      //캐시 히트 +1
      answer += 1;
    } else {
      //캐시가 꽉차있다면, 가장오래된 도시 제거
      if (cache.length === cacheSize) {
        cache.shift();
      }
      //새도시를 캐시에추가
      cache.push(city);
      //캐시미스 +5
      answer += 5;
    }
  }
  return answer;
}
