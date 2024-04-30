package Programmers.lv3;

import java.util.*;

public class 윤찬_Day07_불량사용자 {

    class Solution {

        int answer = 0;
        String[] users;
        Set<String> set;
        boolean[] check;

        public int solution(String[] user_id, String[] banned_id) {

            users = user_id;
            set = new HashSet<>();
            check = new boolean[user_id.length];
            matches(banned_id, 0, new Stack<String>());


            return set.size();
        }

        public void matches(String[] banned_id, int depth, Stack<String> l) {
            if(banned_id.length == depth){
                String setString = "";
                String[] str = l.stream().sorted().toArray(String[]::new);
                for(int i =0 ; i < str.length; i++){
                    //System.out.print(str[i] + ", ");
                    setString += str[i];
                }
                //System.out.println();

                //System.out.println("setString: " + setString);
                set.add(setString);

                return;
            }

            String m = banned_id[depth].replace('*', '.');

            for(int i = 0; i < users.length; i++) {

                if(users[i].matches(m)) {
                    if(!check[i]) {
                        l.push(users[i]);
                        check[i] = true;
                        matches(banned_id, depth + 1, l);

                        if(!l.isEmpty()) l.pop();
                        check[i] = false;
                    }
                }
            }
        }




    }

}
