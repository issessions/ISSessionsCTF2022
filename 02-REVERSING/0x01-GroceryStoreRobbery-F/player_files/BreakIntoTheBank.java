import java.util.*;public class Main{public static void main (String[]args){Scanner myObj = new Scanner (System.in);System.out.println("Only Authorized Bank Personnel are allowed access to this register! What is your password?");
    String input = myObj.nextLine ();
    int pass[] = {
      0x6e,
      0x6c,
      0x6d,
      0x68,
      0x66,
      0x7A,
      0x40,
      0x57,
      0x45,
      0x78,
      0x7b,
      0x6c,
      0x71,
      0x5c,
      0x6a,
      0x70,
      0x5c,
      0x6a,
      0x77,
      0x70,
      0x5c,
      0x6c,
      0x74,
      0x6d,
      0x5c,
      0x6a,
      0x6d,   
      0x75,
      0x66,
      0x71,
      0x70,
      0x66,
      0x22,
      0x7e
    };

    a = 0x6e^3
    for (int i =     0; i < pass.    length;     i++){
      if (input.charAt (i) != (pass[i] ^ 0x0003)){System 
    .out.
	      println
	      ("INCORRECT PASSWORD, AUTHORITIES ARE ON ROUTE! YOU NO TAKE BANANA!!");
	  }
      }
    System.out.
    println ("Welcome Authorized User!");
  }
}	