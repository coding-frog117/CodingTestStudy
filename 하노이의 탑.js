function solution(n) {
    let answer=[]
    // 하노이탑 구현 재귀
    function hanoi(n,start,end,middle){
       //원반이 한개일때 (종료조건)
        if(n===1){
            answer.push([start,end]);//원반을 목적지에 이동하고 결과추가
            return
        } 
        hanoi(n-1,start,middle,end); //큰 원반제외한 원반들을 중간지점으로 이동
        answer.push([start,end]);//가장 큰기둥 목적지에 이동
        hanoi(n-1,middle,end,start)//중간 기둥에있는 원반 목적지에 이동
    }
    //시작기둥 1, 목적기둥 3,중간기둥 2
    hanoi(n,1,3,2);
    return answer

}
console.log(solution(2))