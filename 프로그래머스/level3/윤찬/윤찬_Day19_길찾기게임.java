package Programmers.lv3;

import java.util.*;

public class 윤찬_Day19_길찾기게임 {

    class Solution {

        public int[][] solution(int[][] nodeinfo) {
            int[][] answer = {};

            Node root = null;

            Node[] nodes = new Node[nodeinfo.length];
            for(int i = 0; i < nodeinfo.length; i++) {
                nodes[i] = new Node(nodeinfo[i][0], nodeinfo[i][1], i + 1);
            }

            Arrays.sort(nodes, (o1, o2) -> o2.y - o1.y);

            for(Node node: nodes) {
                if(root == null) {
                    root = node;
                }else {
                    root.getNode(node);
                }
            }

            List<Integer> pre = new ArrayList<>();
            List<Integer> post = new ArrayList<>();
            root.preOrder(pre);
            root.postOrder(post);

            answer = new int[][] { pre.stream().mapToInt(Integer::intValue).toArray(), post.stream().mapToInt(Integer::intValue).toArray()  };

            return answer;
        }
    }


    class Node {
        int x;
        int y;
        int value;

        Node left;
        Node right;

        //List<Integer> pre = new ArrayList<>();
        //List<Integer> post = new ArrayList<>();

        public Node(int x, int y, int value) {
            this.x = x;
            this.y = y;
            this.value = value;
        }

        public void getNode(Node node) {
            if(this.x > node.x) {
                if(left == null) {
                    left = node;
                }else {
                    left.getNode(node);
                }
            }else {
                if(right == null) {
                    right = node;
                }else {
                    right.getNode(node);
                }
            }
        }

        public void preOrder(List<Integer> list) {
            //System.out.println("Node(" + x + ", " + y + ", " + value + ")");
            list.add(this.value);
            if(left != null) {
                //System.out.print("left: ");
                left.preOrder(list);
            }
            if(right != null) {
                //System.out.print("right: ");
                right.preOrder(list);
            }
        }

        public void postOrder(List<Integer> list){
            if(left != null) {
                left.postOrder(list);
            }
            if(right != null) {
                right.postOrder(list);
            }
            list.add(this.value);
        }
    }
}
