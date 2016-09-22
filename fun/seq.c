#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

	char *in = argv[1];
	
	int longestSeq, currSeq = 0;
	int start, end, currS, currE;

	for (int i = 0; in[i] != '\0'; i++) {
		if (in[i] == '1') {
			// init
			if (currSeq == 0) {
				currS = i;
			}
			// change seq
			currE = i;
			currSeq += 1;

			// check if new sequence is larger than prev
			if (currSeq > longestSeq) {
				longestSeq = currSeq;
				start = currS;
				end = currE;
			}

		} else {
			// reset
			currSeq = 0;
			currS = -1;
			currE = -1;
		}
	}

	printf("longestSeq = %d, start: %d, end: %d\n", longestSeq, start, end);

	return EXIT_SUCCESS;
}