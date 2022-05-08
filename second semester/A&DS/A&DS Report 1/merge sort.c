#include <stdio.h>
#include <string.h>
int main() {
    char ch, word[100];
    scanf("%s %s", &ch, &word);
    int idx = 0;
    while(idx < strlen(word)){
        if(word[idx] == ch){
            printf("%d ", idx);
        }
        idx++;
    }
    return 0;
}
