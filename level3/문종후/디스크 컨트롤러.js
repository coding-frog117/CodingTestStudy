function solution(jobs) {
let curr=0;//인덱스
let time=0;//현재시간
let totalTime=0;//총걸린시간
const length=jobs.length;//작업개수
jobs.sort((a,b)=>a[0]-b[0]);//요청시간순으로 작업정렬
const queue=[];
//모든작업을 처리할떄까지 반복
while(jobs.length>curr||queue.length){
    //현재 시간 이후 요청작업있다면 큐에 추가
    if(jobs.length>curr && time>=jobs[curr][0]){
        queue.push(jobs[curr]);
        curr++
        queue.sort((a,b)=>a[1]-b[1])// 처리기시간 기준으로 정렬
        continue;
    }
    //큐가 비어있으면 현재시간을 다음 작업의 요청시간으로 설정
    if(!queue.length){
        time=jobs[curr][0]
    } else {
        //최우선순위 작업을 처리
        const priority=queue.shift();
        totalTime+=time-priority[0]+priority[1];
        //현재시간을 작업종료시간
        time+=priority[1]
    }
}
return Math.floor(totalTime/length)
}

console.log(solution([[0, 3], [1, 9], [2, 6]]))