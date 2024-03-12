public class dout {
    public static void main(String args[]){
        pat1();
    }
    public static void  pat1(){
        for(int i=6;i>0;i--){
            for(int s =0;s<i;s++){
                System.out.print("   ");
            }
            for(int j=6;j>i;j--){   
                System.out.print("* ");
            }
           
        System.out.println();
        }
    }

    public static void  pat2(){
        int  temp =10*-15;
        for(int i=0;i<36;i++){
            for(int j=0;j<i;j++){
               
                System.err.print(temp+" ");
                temp ++;
            }
          

            System.out.println();
        }
    }
}
