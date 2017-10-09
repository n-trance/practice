import java.util.*;
class Unique {
	
	public static boolean unique(String s) {
		Hashtable<Character, Boolean> char_hash = new Hashtable<Character, Boolean>();
		char[] char_string = s.toCharArray();
		
		for (int i = 0; i < char_string.length; i++) {
			char c = char_string[i];
			if (char_hash.containsKey(c)) {
				return false;
			} else {
				char_hash.put(c, true);
			}
		}

		return true;
	}

	// no additional data structure
	// n^2 solution where you check all subsequent string
	// nLogn + n solution if you do a merge sort then check every next str.
	public static boolean uniqueN(String s) {
		char[] char_string = s.toCharArray();
		
		if (char_string.length <= 1) return true;
		for (int i = 0; i < char_string.length - 1; i++) {
			for (int k = i + 1; k < char_string.length; k++) {
				if (char_string[i] == char_string[k]) {
					return false;
				}
			}
		}
		return true;
	}

	public static void main(String args[]) {
		System.out.println(unique("he"));
		System.out.println(unique("bananan"));

		System.out.println(uniqueN("he"));
		System.out.println(uniqueN("bananan"));
	}

}
