import java.util.*;

public class HashTest {

  public static void main(String[] args) {

    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    map.put(1, 0);
    map.put(2, 2);

    System.out.println(map);
    System.out.println(map.get(1));
    System.out.println(map.containsKey(1));
    System.out.println(map.containsKey("3"));

  }

}
