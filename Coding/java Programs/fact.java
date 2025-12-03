import java.util.Scanner;
public class fact{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();   
        int fact = 1;
        if(n>1){
            for(int i = 1; i <= n; i++){
                fact *= i;  
            }
            System.out.println("Factorial of " + n + " is: " + fact);
        } else if (n == 0 || n == 1) {
            System.out.println("Factorial of " + n + " is: 1");
        } else {
            System.out.println("Factorial is not defined for negative numbers.");
        }
    }
}