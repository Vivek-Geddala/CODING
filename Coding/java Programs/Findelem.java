import java.util.Scanner;
class Findelem{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int n=sc.nextInt();
        System.out.println("Enter the elements of the array:");
        int arr[] = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        int find=3;
        for(int i=0;i<=n;i++){
            if(arr[i]==find){
                System.out.println("Element found at index: " + i);
                return;
            }
        }
    }
}