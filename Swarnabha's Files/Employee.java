import java.io.*;
public class Employee
{String name;
    double basic,hra,da,pf,gross,net;
    long empno;
    Employee(String nm,Long en,double b)
    {name=nm;empno=en;
        basic=b;
        
    }
    public void compute()
    {da=(30*basic)/100;
        hra=(15*basic)/100;
        pf=(12*basic)/100;
        gross=basic+da+hra;
        net=gross-pf;
    }
    public void display()
    {System.out.println("The name of the employee is"+name);
        System.out.println("employee no is"+empno);
        System.out.println("Thenet salary is"+net);
    }
    public static void main(String a[])throws IOException
    {BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the name,empno,basic");
        String nm=in.readLine();
        Long en=Long.parseLong(in.readLine());
        double b=Double.parseDouble(in.readLine());
        Employee obj=new Employee(nm,en,b);
        obj.compute();
        obj.display();
    }
}
        
        
        