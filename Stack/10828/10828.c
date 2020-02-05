#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _Node {
    int data;
    struct _Node *next;
}Node;
int size = 0;

void push(Node* stack, int data) {
    Node *temp = (Node *)malloc(sizeof(Node));
    temp.data = data;
    temp.next = NULL;

    if(stack == NULL) {
        stack = temp;
    }
    else {
        stack->next = node;
    }

    return temp;
}

int main() {
    Node* stack = NULL;
    int N = 0;

    for(int i=1; i<=N; i++) {
        char* order_str = (char *)malloc(sizeof(char*5));
        if(strcmp(scanf("%s",order_str), "push")==0) {
            print("aa");
        }

        free(order_str);
    }

    return 0;
}