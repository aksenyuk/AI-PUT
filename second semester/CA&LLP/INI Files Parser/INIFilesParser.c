#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<ctype.h>

int checker (char *line){
    int kek = 1;
    if (isalnum(line[0]) != 0 || line[0] == '[' )
        if (isalnum(line[strlen(line) - 2]) != 0 || line[strlen(line) - 2] == ']' )
            for(int i = 1; i < (strlen(line) - 3); i++){
                    if(isalnum(line[i]) == 0 && line[i] != '-') {
                        kek = 0;
                        break;
                    }
            }
    return kek;
}

int main (int argc, char *argv[])
{
    struct content{
        char key[30];
        char value[30];
    };

    struct section{
        char name[30];
        struct content components[30];
    };

    char req_section[30], req_key[30];
    sscanf(argv[2], "%[^.]. %s", req_section, req_key);

    FILE *input_file;
    input_file = fopen(argv[1], "r");

    char line[30];
    int idx = -1, idx2 = 0;
    char ch_key[30], ch_value[30];
    struct section wszystko[30];

    while(fgets(line, sizeof line, input_file)){
        if(line[0] == '[' && line[strlen(line) - 2] == ']'){
            idx++;
            idx2 = 0;
            strcpy(wszystko[idx].name, line);
            if(checker(line) == 0){
                printf("Detected invalid identifier in name %s\n", line);
            }
        }
        if(line[0] != ';' && line[0] != '#' && sscanf(line, " %s = %s", ch_key, ch_value) == 2){
            strcpy(wszystko[idx].components[idx2].key, ch_key);
            strcpy(wszystko[idx].components[idx2].value , ch_value);
            idx2++;
            if(checker(ch_key) == 0){
                printf("Detected invalid identifier in key %s\n", ch_key);
            }
        }
    }


    char check_sec[30];
    int flag = 0, flag2 = 0;
    
    for(int i = 0; i < 30; i++){
      sscanf(wszystko[i].name, " [%[^]]", check_sec);
        if(strcmp(req_section, check_sec) == 0){
            flag = 1;
            for(int j = 0; j < 30; j++){
                if(strcmp(req_key, wszystko[i].components[j].key) == 0){
                    flag2 = 1;
                    printf("%s\n", wszystko[i].components[j].value);  
            break;
                }
            }
        }
    }
    
    if(flag == 0)
      printf("Failed to find section [%s]\n", req_section);
      
    if(flag2 == 0)
      printf("Failed to find key '%s' in section [%s]\n", req_key, req_section);

    fclose(input_file);
    return 0;
}
