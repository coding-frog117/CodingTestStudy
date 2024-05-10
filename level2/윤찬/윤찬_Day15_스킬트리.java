package Programmers.lv2;

public class 윤찬_Day15_스킬트리 {
  class Solution {
    public int solution(String skill, String[] skill_trees) {
            int answer = 0;

            boolean[] check;
            char[] c = skill.toCharArray();
            for(String skill_tree: skill_trees) {
                check = new boolean[26];
                boolean available = true;

                for(char s: skill_tree.toCharArray()){
                    if(skill.contains(String.valueOf(s)))
                        for(int i = 0; i < skill.indexOf(s); i++) {
                            if(!check[c[i] - 'A']) {
                                available = false;
                            }
                        }
                        if(available){
                            check[s - 'A'] = true;
                        }
                    }
                }

                if(available){
                    answer++;
                }


            }

    return answer;
  }
}}
