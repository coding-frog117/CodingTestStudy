package Programmers.lv3;
import java.util.*;

public class 윤찬_Day03_디스크컨트롤러 {

    class Solution {
        public int solution(int[][] jobs) {
            //작업 요청 시간
            int answer = 0;

            //총 걸린 시간
            int time = 0;

            //요청 시간 순서로 정렬
            PriorityQueue<int[]> pq = new PriorityQueue<>((o1,o2) -> {
                return o1[0] - o2[0];
            });

            //작업 크기 순으로 정렬
            PriorityQueue<int[]> size_pq = new PriorityQueue<>((o1, o2) -> {
                return o1[1] - o2[1];
            });

            //시간 요청 순으로 먼저 모든 작업을 넣기
            for(int[] job: jobs){
                //System.out.println("job: [" + job[0] +"," + job[1] + "]");
                pq.add(job);
            }

            //두 큐가 모두 비어있을 때까지 반복하기
            while(!pq.isEmpty() || !size_pq.isEmpty()) {

                //해당 시점 안에 있는 시간 요청 작업 넣기
                while( !pq.isEmpty()  && pq.peek()[0] <= time) {
                    //System.out.println("time: " + time +", insert size_pq job: [" + pq.peek()[0] +"," + pq.peek()[1] + "]");
                    size_pq.add(pq.poll());
                }

                //위에 시간 작업을 넣었는데 비어있는 경우 그 다음 작업 요청 시간대로 이동하기
                if(size_pq.isEmpty()) {
                    int[] job = pq.poll();
                    time = job[0];
                    //System.out.println("new time job: [" + job[0] +"," + job[1] + "], time: " + time);
                    size_pq.add(job);
                }else {
                    //작업 요청 시간 구하기
                    int[] job = size_pq.poll();
                    //System.out.println("add answer job: [" + job[0] +"," + job[1] + "], time: " + time);

                    //작업 시간 + 대기 시간 더하기
                    answer += (time - job[0]) + job[1];
                    //System.out.println("answer : " + answer);

                    //현재 시간에서 작업 시간 더하기
                    time += job[1];
                }
            }

            //평균값 반환
            return answer/jobs.length;
        }
    }
}
