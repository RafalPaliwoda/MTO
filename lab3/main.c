#include <stdio.h>
#include <string.h>

int my_printf(char *format_string, char *param){
	for(int i=0;i<strlen(format_string);i++){
		if((format_string[i] == '#')){
			if ((format_string[i+1] == '.') && isdigit(format_string[i+2]) && (format_string[i+3] == 'k')){
				char vartable[5];
				sprintf(vartable, "%%.%cs", format_string[i+2]);
				printf(vartable,param);
				i+=3;
			}
			if (isdigit(format_string[i+1]) != 0){
				int num = 0;
				while (format_string[i+1+num] != 'k'){
					num++;
				}
				char tab[num];
				for (int x = 0; x < num; x++){
					tab[x] = format_string[i+1+x];
				}
				int z = num;
			 	num = atoi(tab);
				if (strlen(param) - 1 < num){
					for (int x = 0; x < num - strlen(param) - 1; x++){
						printf(" ");
					}
					for ( int x = 0; x < num; x++){
						if (param[x] >= 65 && param[x] <= 90){
							putchar(param[x]+32);
						}
						else if (param[x] >= 97 && param[x]<= 122){
							putchar(param[x]-32);
						}
						else{
							putchar(param[x]);
						}
					}
				}
				else{
					for ( int x = 0; x < num; x++){
						if (param[x] >= 65 && param[x] <= 90){
							putchar(param[x]+32);
						}
						else if (param[x] >= 97 && param[x]<= 122){
							putchar(param[x]-32);
						}
						else{
							putchar(param[x]);
						}
					}
				}
				printf(" ");
				i+=z;
				i+=2;
			}
		}else
			if (format_string[i] >= 65 && format_string[i] <= 90){
				putchar(format_string[i]+32);
			}
			else if (format_string[i] >= 97 && format_string[i] <= 122){
                putchar(format_string[i]-32);
            }
			else{
				putchar(format_string[i]);
			}

	}
	puts("");
}

int main(int argc, char *argv[]){
	char buf[1024],buf2[1024];
	while(gets(buf)){
		gets(buf2);
		my_printf(buf,buf2);
	}
	return 0;
}
