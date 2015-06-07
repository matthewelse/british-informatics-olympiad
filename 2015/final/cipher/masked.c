#include <stdio.h>
#include <stdlib.h>
FILE *fin, *fout;

int main(int argc, char** argv) {
	char str[1000000];
	fin = fopen("input.txt", "rb");
	fout = fopen("output.txt", "wb");
	
	int i = 0;
	int c; 
	while ((c = fgetc(fin)) != EOF) { 
		str[i] = c;
		i++;
	}
		
	for (int j = 0; j < i; j++) {
		if (str[j] == 'M' || str[j] == 'm') {
			// start of the string...
			int n = 0;
			for (int k = 1; k <= 5; k++) {
				if (str[j+k] < 91) {
					// caps
					n += 1 << (5-k);
				}
			}
			fputc(n+(str[j] == 'M' ? 64 : 96), fout);
			
			j += 5;
		}
		else {
			fputc(str[j], fout);
		}
	}
	
	return 0;
}