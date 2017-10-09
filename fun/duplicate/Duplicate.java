import java.util.*;
class Duplicate {
	
	public static String undupe(String str) {
		char[] s = str.toCharArray();
		// case single char or empty
		if (s.length < 2) {
			return String.valueOf(s);
		}
		
		// case 2 or more char
		int tail = 1;
		
		// traverse tail length
		for (int i = 1; i < s.length; i++) {
			for (int k = 0; k < tail; k++) {
				if (s[i] == s[k]) {
					break;
				}
				if (k == tail) {
					s[tail] = s[i];
					tail++;
				}
			}
		}
		s[tail] = '\0';
		return String.valueOf(s);
	}

	public static void main(String args[]) {
		System.out.println(undupe("a"));
		System.out.println(undupe("ab"));
		System.out.println(undupe("aba"));
		System.out.println(undupe("abb"));
		System.out.println(undupe("banana"));
	}

}
