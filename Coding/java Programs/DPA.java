import java.util.*;
class DPA{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number:");
        int n=sc.nextInt();
        int result = DPA(n);
        System.out.println("Ways: " + result);
    }
public static int DPA(int n){
        if(n == 0 || n == 1){
            return 1;
        } else {
            int[] dp = new int[n + 1];
            dp[0] = 1;
            dp[1] = 1;
            for(int i = 2; i <= n; i++){
                dp[i] = dp[i - 1] + dp[i - 2];
            }
            return dp[n];
        }
    }
}