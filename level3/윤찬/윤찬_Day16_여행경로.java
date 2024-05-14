package Programmers.lv3;

import java.util.*;

public class 윤찬_Day16_여행경로 {
    class Solution {

        Map<String, Integer> city;
        List<String>[] list;
        List<String> answer;

        public String[] solution(String[][] tickets) {
            answer = new ArrayList<>();

            city = new HashMap<>();

            int index = 0;
            for(String[] ticket : tickets) {
                for(String c : ticket){
                    if(city.get(c) == null){
                        System.out.println(c + " : " + index);
                        city.put(c, index);
                        index++;
                    }
                }
            }

            list = new ArrayList[city.size()];
            for(int i = 0; i < city.size(); i++){
                list[i] = new ArrayList<>();
            }

            for(String[] ticket: tickets) {
                list[city.get(ticket[0])].add(ticket[1]);
            }

            for(int i = 0; i < city.size(); i++){
                Collections.sort(list[i]);
            }

            // for(int i = 0; i < city.size(); i++) {
            //     System.out.print(i + " : ");
            //     for(String c: list[i]) {
            //         System.out.print(c + " ");
            //     }
            //     System.out.println();
            // }

            //bfs("ICN");
            dfs("ICN", new ArrayList<>(), list);
            return answer.stream().toArray(String[]::new);
        }

//     public void bfs(String start){
//         Queue<String> queue = new LinkedList<>();
//         //answer.add(start);
//         queue.add(start);

//         while(!queue.isEmpty()) {
//             String s = queue.poll();
//             answer.add(s);
//             int index = city.get(s);
//             if(!p[index].isEmpty()) {
//                 queue.add(p[index].poll());
//             }
//         }
//     }

        public void dfs(String start, List<String> route, List<String>[] tickets) {
            if(Arrays.stream(tickets).allMatch( t -> t.isEmpty() )) {
                if(answer.isEmpty()){
                    answer = route;
                }
            }
            List<String> t = tickets[city.get(start)];
            for(int i = 0; i < t.size() ; i ++) {
                t.remove(t.get(i));
                //dfs(t.get(i), Arrays.copyOf(route), tickets);
                t.add(i,t.get(i));
            }

        }
    }
}
