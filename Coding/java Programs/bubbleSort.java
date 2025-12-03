class bubbleSort{
    public static void main(String[] args){
        int[]arr={64,34,25,12,22,11,90};
        System.out.println("Original array:");  
        for(int i=0;i<arr.length;i++){  
            System.out.print(arr[i] + " ");  
        }
        System.out.println("\n");
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length-1  -i;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
        System.out.println("Sorted array:");
        for(int i=0;i<arr.length;i++){  
            System.out.print(arr[i] + " ");
        }
    }
}