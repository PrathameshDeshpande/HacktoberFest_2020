import java.io.*;
public class billelectric                                               //name of class                                           
{public void found()throws IOException                   //name of method                           
    {BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the number of units consumed");      //accepting the units consumed
        Double u=Double.parseDouble(in.readLine()); 
        System.out.println("Rental for each month is Rs 250");
        double a,b,t;
        if(u<=100)
        t=u*0.5;
        else
        if(u>=101 && u<=250)
        t=100*0.5+0.75*(u-100);
        else
        if(u>=251 && u<=400)
        t=100*0.5+150*0.75+1*(u-250);
        else
        t=100*0.5+150*0.75+150*1+1.5*(u-400);
        t=t+250;
        System.out.println("Taxes for the entered units is with the rental is :"+t); //printing the tax value
    }                                                                  //end of method
}                                                                      //end of class