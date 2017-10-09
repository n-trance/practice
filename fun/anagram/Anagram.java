import java.util.*;

class Anagram {
	
	public static boolean is_anagram(String str1, String str2) {
		char[] s1 = str1.toCharArray();
		char[] s2 = str2.toCharArray();
		Hashtable<Character, Integer> hash = new Hashtable<Character, Integer>();

		// length has to be equal
		if (s1.length != s2.length) return false;

		// build hash
		for (int i = 0; i < s1.length; i++) {
			char c = s1[i];
			if (hash.containsKey(c)) {
				// increment character count
				hash[c]++;
			} else {
				// initial character count
				hash.put(c, 1);
			}
		}

		// check hash with str2
		for (int i = 0; i < s2.length; i++) {
			char c = s2[i];
			if (hash.containsKey(c)) {
				// if count < 0, then false
				hash[c]--;
				if (hash[c] < 0) return false;
			} else {
				// c not in hash, therefore false
				return false;
			}
		}

		return true;
	}

	public static void main(String args[]) {

	}

}
