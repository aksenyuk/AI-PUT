#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<ctype.h>
#include <time.h>

struct student {
    char name[13];
    char sur[13];
    int index;
};

struct node{
    struct student data;
    struct node *right;
    struct node *left;
};

struct node* new_node(int index, char name[13], char sur[13]){
    struct node *p;
    p = (struct node *)malloc(sizeof(struct node));
    p->data.index = index;
    strcpy(p->data.name, name);
    strcpy(p->data.sur, sur);
    p->left = NULL;
    p->right = NULL;
    return p;
}

struct node* add(struct node *sroot, int index, char name[13], char sur[13]){
    if(sroot==NULL)
        return new_node(index, name, sur);
    else if(index > sroot->data.index)
        sroot->right = add(sroot->right, index, name, sur);
    else
        sroot->left = add(sroot->left, index, name, sur);
    return sroot;
}

struct node* search(struct node *sroot, int result){
    if(sroot==NULL){
        printf("No student with index: %d\n", result);
        return 0;
    }
    if(sroot->data.index == result){
        printf("Found: %s %s, %d\n", sroot->data.name, sroot->data.sur, sroot->data.index);
        return 0;
    }
    if(result>sroot->data.index)
        search(sroot->right, result);
    else if(result<sroot->data.index)
        search(sroot->left, result);
};

struct node* most_left(struct node *sroot)
{
    if(sroot == NULL)
        return 0;
    else if(sroot->left != NULL)
        return most_left(sroot->left);
    return sroot;
}

struct node* del(struct node *sroot, int usun)
{
    if(sroot==NULL)
        return 0;
    else if (usun>sroot->data.index)
        sroot->right = del(sroot->right, usun);
    else if(usun<sroot->data.index)
        sroot->left = del(sroot->left, usun);
    else{
        if(sroot->left==NULL && sroot->right==NULL){
            free(sroot);
            return 0;
        }
        else if(sroot->left==NULL || sroot->right==NULL){
            struct node *temp;
            if(sroot->left==NULL)
                temp = sroot->right;
            else
                temp = sroot->left;
            free(sroot);
            return temp;
        }
        else{
            struct node *temp = most_left(sroot->right);
            sroot->data.index = temp->data.index;
            sroot->right = del(sroot->right, temp->data.index);
        }
    }
    return sroot;
}

void rearr(struct node *sroot){
    if(sroot!=NULL){
        rearr(sroot->left);
        rearr(sroot->right);
    }
}



int main()
{
    FILE *input_file;
    input_file = fopen("C:/Users/1625203/Desktop/A&DS Report 2/meow2.txt", "r");
    char line[100], name[13], sur[13],  index[8];

    struct node *sroot;
    fgets(line, sizeof line, input_file);
    sscanf(line, "%s %s %s", name, sur, index);
    sroot = new_node(atoi(index), name, sur);

    while(fgets(line, sizeof line, input_file)){
        sscanf(line, "%s %s %s", name, sur, index);
        add(sroot, atoi(index), name, sur);
    }
    //add(sroot, 6652982, "Grzegorz", "Pawlak");
    //search(sroot, 6652982);
    //del(sroot, 6652982);
   // search(sroot, 6652982);


    clock_t tic = clock();
    for(int i = 0; i < 1000; i++){
        del(sroot, rand() % (9999999 + 1 - 1000000) + 1000000);
    }

    clock_t toc = clock();
	printf("%f\n", (double)(toc - tic) / CLOCKS_PER_SEC);

    return 0;
}
