import java.util.Scanner;
class Largenum{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n;
        System.out.print("Enter the number of elements: ");
        n=sc.nextInt();
        int a[] = new int[n];
        for(int i=0;i<n;i++){
            System.out.print("Enter number " + (i+1) + ": ");
            a[i] = sc.nextInt();
        }
    
        int max=a[0];
        for(int i=1;i<n;i++){
            if(a[i]>max){
                max=a[i];
            }
        }   
        System.out.println("Largest number is: " + max);
    }
}