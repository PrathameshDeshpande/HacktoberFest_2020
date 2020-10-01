import java.io.*;
public class automorp
{public void main()throws IOException
    {BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
        int n;
        int f=0,s;
     for(n=10;n<=100;n++)
       {s=n*n;
       do
        {
            if(n%10!=s%10)
            {f=1;
                break;
            }
            else
            {n=n/10;
                s=s/10;
            }
        }while(n>0);
        if(f==0)
        System.out.println(s);
        
    }
}
}
