#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _Node {
	int data;
	struct _Node *next;
}Node;
int size = 0;

void push(Node** queue, int data);
int pop(Node** queue);
int isEmpty(Node* queue);
int front(Node* queue);
int back(Node* queue);

int main() {
	Node* queue = NULL;
	int N = 0;
	int order_data = 0;

	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		char* order_str = (char *)malloc(sizeof(char)*6);

		scanf("%s", order_str);
		if (strcmp(order_str, "push") == 0) {
			scanf("%d", &order_data);
			push(&queue, order_data);
		}
		else if (strcmp(order_str, "pop") == 0) {
			printf("%d\n", pop(&queue));
		}
		else if (strcmp(order_str, "size") == 0) {
			printf("%d\n", size);
		}
		else if (strcmp(order_str, "empty") == 0) {
			printf("%d\n", isEmpty(queue));
		}
		else if (strcmp(order_str, "front") == 0) {
			printf("%d\n", front(queue));
		}
		else {
			printf("%d\n", back(queue));
		}

		free(order_str);
	}

	return 0;
}

void push(Node** queue, int data) {
	size++;
	Node *temp = (Node *)malloc(sizeof(Node));
	temp->data = data;
	temp->next = NULL;

	if (*queue == NULL) {
		*queue = temp;
		return;
	}
	else {
		Node *cur = *queue;

		while (cur->next != NULL)
			cur = cur->next;

		cur->next = temp;
		return;
	}
}
int pop(Node** queue) {
	if (*queue == NULL)
		return -1;
	else {
		size--;
		Node* temp_Node = *queue;
		*queue = (*queue)->next;

		int temp_data = temp_Node->data;
		free(temp_Node);

		return temp_data;
	}
}
int isEmpty(Node* queue) {
	if (queue == NULL)
		return 1;
	else
		return 0;
}
int front(Node* queue) {
	if (queue == NULL)
		return -1;
	else
		return queue->data;
}
int back(Node* queue) {
	if (queue == NULL)
		return -1;
	else {
		Node* cur = queue;

		while (cur->next != NULL)
			cur = cur->next;

		return cur->data;
	}
}