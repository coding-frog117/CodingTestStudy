package Programmers.lv3;

public class 윤찬_Day06_기지국설치 {

    class Solution {
        public int solution(int n, int[] stations, int w) {
            int answer = 0;

            int start = 1;
            for(int station: stations) {
                int end = station - w;
                if(start < end){
                    answer += (int)Math.ceil( (end - start) / (2.0*w + 1) ); //(end - start) % (2 * w + 1) == 0 ? (end - start) / (2 * w + 1) : (end - start) / (2 * w + 1) + 1;
                }
                start = (station + w + 1);
            }

            if(start < n + 1) {
                //System.out.println("start: "+ start + ", n: " + n);
                answer += (int)Math.ceil( (n + 1 - start) / (2.0*w + 1) );//(n + 1 - start) % (2 * w + 1) == 0 ? (n + 1 - start) / (2 * w + 1) : (n + 1 - start) / (2 * w + 1) + 1;
            }

            return answer;
        }
    }

}
