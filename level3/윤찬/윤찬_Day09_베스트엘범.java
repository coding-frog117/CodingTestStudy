package Programmers.lv3;

import java.util.*;
public class 윤찬_Day09_베스트엘범 {

    class Solution {
        Map<String, Music> map = new HashMap<>();


        public int[] solution(String[] genres, int[] plays) {

            for (int i = 0; i < genres.length; i++) {
                if (!map.containsKey(genres[i])) {
                    map.put(genres[i], new Music(genres[i], plays[i], i));
                } else {
                    map.get(genres[i]).addPlay(plays[i], i);
                }
            }

            List<Integer> result = new ArrayList<>();

            List<Music> music_list = new ArrayList<>(map.values());
            music_list.stream().sorted().forEach((m) -> {
                //System.out.println(m.genres + " " + m.sum);
                result.addAll(m.getPlay());
            });
//        priorityQueue.forEach((m) -> {
//            result.addAll(m.getPlay());
//        });

            return result.stream().mapToInt(Integer::intValue).toArray();
        }
    }

    class Music implements Comparable<Music> {
        String genres;
        int sum = 0;
        List<PlayInfo> plays = new ArrayList<>();

        public Music(String genres, int play, int index) {
            this.genres = genres;
            sum += play;
            plays.add(new PlayInfo(index, play));
        }

        public void addPlay(int play, int index) {
            sum += play;
            plays.add(new PlayInfo(index, play));
        }

        public List<Integer> getPlay() {
            PriorityQueue<PlayInfo> priorityQueue = new PriorityQueue<>();
            priorityQueue.addAll(plays);

            List<Integer> result = new ArrayList<>();

            while (!priorityQueue.isEmpty()){

                if(result.size() == 2){ break; }

                result.add(priorityQueue.poll().index);
            }
            return result;
        }

        @Override
        public int compareTo(Music o) {
            return o.sum - this.sum;
        }
    }

    class PlayInfo implements Comparable<PlayInfo> {
        int index;
        int play;

        public PlayInfo(int index, int play) {
            this.index = index;
            this.play = play;
        }

        @Override
        public int compareTo( PlayInfo o) {
            if (this.play == o.play) {
                return this.index - o.index;
            } else {
                return o.play - this.play;
            }
        }
    }
}
