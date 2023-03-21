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

struct node* new_node(int index){
    struct node *p;
    p = (struct node *)malloc(sizeof(struct node));
    p->data.index = index;
    p->left = NULL;
    p->right = NULL;
    return p;
}

struct node* add(struct node *sroot, int index){
    if(sroot==NULL)
        return new_node(index);
    else if(index > sroot->data.index)
        sroot->right = add(sroot->right, index);
    else
        sroot->left = add(sroot->left, index);
    return sroot;
}

struct node* search(struct node *sroot, int result){
    if(sroot==NULL){
        printf("No student with index: %d\n", result);
        return 0;
    }
    if(sroot->data.index == result){
        printf("Found: %d\n", sroot->data.index);
        return 0;
    }
    if(result>sroot->data.index)
        search(sroot->right, result);
    else if(result<sroot->data.index)
        search(sroot->left, result);
};

struct node* most_left(struct node *sroot){
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

struct node* sortedArrayToBST(int arr[], int start, int end)
{
    if (start > end)
      return NULL;

    int mid = (start + end)/2;
    struct node *root = new_node(arr[mid]);

    root->left =  sortedArrayToBST(arr, start, mid-1);

    root->right = sortedArrayToBST(arr, mid+1, end);

    return root;
}



int main()
{
    FILE *input_file;
    input_file = fopen("C:/Users/1625203/Desktop/A&DS I/A&DS Report 2/meow2.txt", "r");
    char line[100], name[13], sur[13],  index[8];
    int indeces[500], idx=0;

    while(fgets(line, sizeof line, input_file)){
        sscanf(line, "%s %s %s", name, sur, index);
        indeces[idx] = atoi(index);
        idx++;
    }

    struct node *sroot = sortedArrayToBST(indeces, 0, idx-1);
    //search(sroot, 5678909);
    //add(sroot, 5678909);
    //search(sroot, 5678909);
    //del(sroot, 5678909);
    //search(sroot, 5678909);

    clock_t tic = clock();
    //for(int i = 0; i < 1000; i++){
        //del(sroot, rand() % (9999999 + 1 - 1000000) + 1000000);
    //}
    search(sroot, 5678909);
    clock_t toc = clock();
	printf("%f\n", (double)(toc - tic) / CLOCKS_PER_SEC);

    return 0;
}
