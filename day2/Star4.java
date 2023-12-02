import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.Map;
import java.util.HashMap;

public class Star4 {
  public static void main(String[] args) {
    try {
      File myObj = new File("input.txt");
      Scanner myReader = new Scanner(myObj);
      String str_num = "0";
      int num = -1;
      Map<Character, Integer> mins = new HashMap<Character, Integer>();
      int res = 0;
      while (myReader.hasNextLine()) {
        String line = myReader.nextLine();
        mins.put('b', 0);
        mins.put('r', 0);
        mins.put('g', 0);
        for (int i = 0; i < line.length(); i++) {
            char ch = line.charAt(i);
            if (ch <= '9' && ch >= '0') {
                str_num += ch;
            } else if (ch == ' ') {
                if (str_num != "0") {
                    num = Integer.parseInt(str_num);
                }
                str_num = "0";
            }
            if (ch == 'b' || ch == 'r' || ch == 'g') {
                if (num > mins.get(ch)){
                    mins.put(ch, num);
                }
                num = -1;
            }
        }
        res += mins.get('b') * mins.get('g') * mins.get('r');
      }
      System.out.println(res);
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}