import java.util.*;
public class Numbers {
    public static void main(String args[]){
       num();
    }
    public static void num(){
        System.out.print("Enter a Number : ");
        Scanner in = new Scanner(System.in);
        int num= in.nextInt();
        in.close();
        int num2 = num;
        int sum=0;
        while(num!=0){
            int temp = num%10;
            sum = sum*10 +temp;
            num = num/10;
        }if(sum==num2){
            System.out.println("Palendrome Number");
        }else{
            System.out.println("Not a Palendrome Number");
        }

       
    }
}