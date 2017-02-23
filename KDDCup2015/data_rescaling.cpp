#include <stdio.h>
#include <string.h>

int main(int argc, char** argv){
	FILE *fp;
	char line[4000];
	char *pch;

	// printf("%d\n", argc);
	fp = fopen(argv[1] , "r");
	while(fgets(line, 4000, fp) != NULL){
		pch = strtok(line, " ");
		printf("%s ", pch);

		pch = strtok(NULL, " ");
		while(pch != NULL){
			int label;
			double value;
			sscanf(pch, "%d:%lf", &label, &value);
			printf("%lf ", value);
			pch = strtok(NULL, " ");
		}
		printf("\n");
	}
}