import java.util.*;

public class Distinct {

  public static void main(String[] args) {

    int[] n = {1,2,3,4,5,10};
    int[] m = {4,5,6,7,8,9,10};

    int count = 0;

    for (int i = 0; i < n.length; i++) {
      // binary search for n[i] in m
      int index = Arrays.binarySearch(m, n[i]);
      if (index > -1) {
        count++;
      }
    }

    System.out.println(count);

  }

}
