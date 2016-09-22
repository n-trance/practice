#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

	char *a = "1002";
	int new = 0;

	for (int i=0; a[i]!='\0'; i++) {
		new *= 10;
		new += a[i] - 48; // convert t ascii value
	}

	printf("%d\n", new);

	return EXIT_SUCCESS;
}