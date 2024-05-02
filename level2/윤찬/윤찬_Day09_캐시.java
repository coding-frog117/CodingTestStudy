package Programmers.lv2;
import java.util.*;
public class 윤찬_Day09_캐시 {

    class Solution {
        public int solution(int cacheSize, String[] cities) {
            int answer = 0;

            Queue<String> queue = new LinkedList<>();

            if(cacheSize == 0 ) return cities.length * 5;

            for(String city: cities) {
                String lowerCity = city.toLowerCase();
                if(queue.contains(lowerCity)){
                    int currentSize = queue.size();
                    for(int i = 0; i < currentSize; i++){
                        String c = queue.poll();
                        if(!c.equals(lowerCity)){
                            queue.add(c);
                        }
                    }
                    queue.add(lowerCity);
                    //System.out.print("exist " + lowerCity +" :");
                    //queue.stream().forEach(c -> System.out.print(c + ", "));
                    //System.out.println();
                    answer +=1;
                }else {
                    if(queue.size() == cacheSize){
                        queue.poll();
                    }
                    queue.add(lowerCity);
                    //System.out.print("new :");
                    //queue.stream().forEach(c -> System.out.print(c + ", "));
                    //System.out.println();
                    answer +=5;
                }

            }

            return answer;
        }

    }
}
