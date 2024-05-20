package Programmers.lv3;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class 윤찬_Day11_섬연결하기 {
    class Solution {
        int[] parent;


        public int solution(int n, int[][] costs) {
            int answer = 0;

            List<int[]> list = Arrays.stream(costs).sorted((o1, o2) -> {
                return o1[2] - o2[2];
            }).collect(Collectors.toList());

            parent = new int[n];
            for(int i = 0; i < n; i++){
                parent[i] = i;
            }

            int count = 0;
            for(int i = 0; i < list.size(); i++){
                int[] values = list.get(i);
                if(find(values[0]) != find(values[1])){
                    union(values[0], values[1]);
                    answer += values[2];
                    count++;
                }

                if(count == n-1) break;
            }

            return answer;
        }

        public void union(int a, int b) {
            // parent[a] = find(a);
            // parent[b] = find(b);
            // if(parent[a] != parent[b]){
            //     parent[b] = parent[a];
            // }
            int root1 = find(a);
            int root2 = find(b);
            parent[root2] = root1;
        }

        public int find(int a) {
            if(parent[a] == a){
                return a;
            }else {
                parent[a] = find(parent[a]);
                return parent[a];
            }
        }
    }
}
