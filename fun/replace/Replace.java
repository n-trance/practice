import java.util.*;

class Replace {

	public static String replace(String str) {
		
		return str.replaceAll(" ", "%20");
	}

	public static void main(String args[]) {
		String n = replace("hello friend");
		System.out.println(n);
	}

}
