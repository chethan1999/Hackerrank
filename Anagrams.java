import java.util.Scanner;

public class Solution {


  public static boolean isAnagram(String a,String b)
  {
      String c1 = a.replace(" ","").toLowerCase();
      String c2 = b.replace(" ","").toLowerCase();
      c1 = c1.toLowerCase();
      c2 = c2.toLowerCase();

      boolean status = true;
      if(a.length()!=b.length())
      {
          status = false;
      }
      else
      {
          char[] ch1 = a.toCharArray();

          for (char c : ch1)
            {
                int index = c2.indexOf(c);
 
                if(index != -1)
                {
 
                    c2 = c2.substring(0, index)+c2.substring(index+1, c2.length());
                }
                else
                {
 
                    status = false;
 
                    break;
                }
            }
      }
      return status;
  }
  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
/*
output:
Input (stdin)
    anagramm
    marganaa

Your Output (stdout)
    Not Anagrams

Expected Output
    Not Anagrams
*/
