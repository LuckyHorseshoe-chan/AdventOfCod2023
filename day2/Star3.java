import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.Map;
import java.util.HashMap;

public class Star3 {
  public static void main(String[] args) {
    try {
      File myObj = new File("input.txt");
      Scanner myReader = new Scanner(myObj);
      String str_num = "0";
      int num = -1;
      int cnt = 0;
      int res = 0;
      Map<Character, Integer> maxs = new HashMap<Character, Integer>();
      maxs.put('b', 14);
      maxs.put('r', 12);
      maxs.put('g', 13);
      while (myReader.hasNextLine()) {
        cnt += 1;
        String line = myReader.nextLine();
        boolean game = true;
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
                if (num > maxs.get(ch)) {
                    game = false;
                    break;
                }
                else {
                    num = -1;
                }
            }
        }
        if (game) {
            res += cnt;
        }
      }
      System.out.println(res);
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}