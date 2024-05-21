package baekjoon;

import java.util.Scanner;

public class pb6198 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] num = new int[n];
        for(int i = 0; i < n; i++) {
            num[i] = sc.nextInt();
        }
        long sum = 0;
        for(int i = 0; i < n; i++) {
            long count = 0;
            //System.out.print("i" + (i+ 1) +" : ");
            for(int j = i + 1; j < n; j++) {
                if(num[i] <= num[j]) {
                    break;
                }else {
                    //System.out.print(j + ", ");
                    count++;
                }
            }
            sum += count;
            //System.out.println();
        }

        System.out.println(sum);
    }
}
