import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.Map;
import java.util.HashMap;

public class Star5 {
  public static boolean isSymbol(char ch) {
    if ((ch < '0' || ch > '9') && ch != '.'){
      return true;
    }
    return false;
  }
  public static boolean isDigit(char ch) {
    if (ch >= '0' && ch <= '9'){
      return true;
    }
    return false;
  }
  public static boolean isPartNum(int[] x, int[] y, String[] window) {
    for (int i = 0; i < x.length; i++){
      if (isSymbol(window[y[i]].charAt(x[i]))){
        return true;
      }
    }
    return false;
  }

  public static void main(String[] args) {
    try {
      File myObj = new File("input.txt");
      Scanner myReader = new Scanner(myObj);
      String[] window = {"", "", ""};
      String str_num = "";
      int res = 0;
      boolean partNum = false;
      int[] x, y;
      for (int i = 0; i < 2; i++){
        window[i] = myReader.nextLine();
      }
      for (int i = 0; i < window[0].length(); i++){
        char ch = window[0].charAt(i);
        if (isDigit(ch)) {
          if (!partNum) {
            if (str_num != ""){
              x = {i};
              y = {1};
            } else{
              x = {i-1, i-1, i};
              y = {0, 1, 1};
            }
            partNum = isPartNum(x, y, window);
          }
          str_num += ch;
        } else if (str_num != "") {
          if (!partNum) {
            x = {i, i};
            y = {0, 1};
            partNum = isPartNum(x, y, window);
          }
          if (partNum){
            res += Integer.parseInt(str_num);
            partNum = false;
          }
        }
      }
      while (myReader.hasNextLine()) {
        String line = myReader.nextLine();
        if (window[2] != ""){
          window[0] = window[1];
          window[1] = window[2]; 
        }
        window[2] = line;
        for (int i = 0; i < window[1].length(); i++){
          char ch = line.charAt(i);
          if (isDigit(ch)) {
            if (!partNum) {
              if (str_num != ""){
                x = {i, i};
                y = {0, 2};
              } else{
                x = {i-1, i-1, i-1, i, i};
                y = {0, 1, 2, 0, 2};
              }
              partNum = isPartNum(x, y, window);
            }
            str_num += ch;
          } else if (str_num != "") {
            if (!partNum) {
              x = {i, i, i};
              y = {0, 1, 2};
              partNum = isPartNum(x, y, window);
            }
            if (partNum){
              res += Integer.parseInt(str_num);
              partNum = false;
            }
          }
        }
      }
      for (int i = 0; i < window[2].length(); i++){
        char ch = window[2].charAt(i);
        if (isDigit(ch)) {
          if (!partNum) {
            if (str_num != ""){
              x = {i};
              y = {1};
            } else{
              x = {i-1, i-1, i};
              y = {2, 1, 1};
            }
            partNum = isPartNum(x, y, window);
          }
          str_num += ch;
        } else if (str_num != "") {
          if (!partNum) {
            x = {i, i};
            y = {2, 1};
            partNum = isPartNum(x, y, window);
          }
          if (partNum){
            res += Integer.parseInt(str_num);
            partNum = false;
          }
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