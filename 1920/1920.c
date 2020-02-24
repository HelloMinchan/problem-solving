#include <stdio.h>
#include <stdlib.h>

typedef struct treeNode {
    int key;
    struct treeNode* left;
    struct treeNode* right;
} treeNode;

treeNode* insertNode(treeNode *p, int num) {
    if (p == NULL) {
	treeNode *newNode = (treeNode*)malloc(sizeof(treeNode));
	newNode->key = num;
	return newNode;
    }
    else if (num < p->key)  p->left = insertNode(p->left, num);
    else if (num > p->key)  p->right = insertNode(p->right, num);

    return p;
}

int searchBST(treeNode* root, int num) {
    treeNode* p;
    p = root;
    while (p != NULL) {
	if (num < p->key) p = p->left;
	else if (num == p->key) return 1;	//있을 때
	else p = p->right;
    }
    return 0;	//없을 때
}

int main() {
    int N = 0, M = 0;
    int key = 0;
    treeNode* root = NULL;

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
	scanf("%d", &key);
	root = insertNode(root, key);
    }

    scanf("%d", &M);
    for (int i = 0; i < M; i++) {
	scanf("%d", &key);
	printf("%d\n", searchBST(root, key));
    }

    return 0;
}
