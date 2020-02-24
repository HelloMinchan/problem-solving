import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        int[] table = new int[11];
        table[1] = 1;
        table[2] = 2;
        table[3] = 4;
        for(int i=4;i<table.length;i++)
            table[i] = table[i-1] + table[i-2] + table[i-3];
        
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int n = 0;
        for(int i=0;i<T;i++) {
            n = sc.nextInt();
            System.out.println(table[n]);
        }
        sc.close();
    }   
}
