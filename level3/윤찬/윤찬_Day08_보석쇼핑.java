package Programmers.lv3;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

public class 윤찬_Day08_보석쇼핑 {

    class Solution {
        public int[] solution(String[] gems) {
            int[] answer = new int[2];

            Set<String> set = new HashSet<>();
            Deque<G> queue = new ArrayDeque<>();

            for(String gem: gems){
                set.add(gem);
            }

            int minLen = Integer.MAX_VALUE;

            // queue.add(new G("DIA", 0));
            // queue.add(new G("DIA2", 1));
            // System.out.println(queue.peekFirst().gem);
            // System.out.println(queue.peekLast().gem);
            int index = 0;
            //System.out.println(set.size());
            while(index != gems.length) {

                if(set.size() != queue.stream().map(g -> g.gem).collect(Collectors.toSet()).size()) {
                    queue.add(new G(gems[index], index));
                    index++;
                }

                if(set.size() == queue.stream().map(g -> g.gem).collect(Collectors.toSet()).size()) {
                    if(queue.peekLast().index - queue.peekFirst().index < minLen) {
                        answer = new int[] { queue.peekFirst().index + 1 , queue.peekLast().index + 1 };
                        minLen = queue.peekLast().index - queue.peekFirst().index;
                    }
                    queue.pollFirst();
                }

            }


            return answer;
        }

        public class G{
            String gem;
            int index;

            public G(String name, int index){
                this.gem = name;
                this.index = index;
            }
        }
    }
}
