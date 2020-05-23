#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _Node {
	int data;
	struct _Node *next;
}Node;
int size = 0;

Node* push(Node* stack, int data);
int pop(Node** stack);
int isEmpty(Node* stack);
int peek(Node* stack);

int main() {
	Node* stack = NULL;
	int N = 0;
	int order_data = 0;

	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		char* order_str = (char *)malloc(sizeof(char)*6);

		scanf("%s", order_str);
		if (strcmp(order_str, "push") == 0) {
			scanf("%d", &order_data);
			stack = push(stack, order_data);
		}
		else if (strcmp(order_str, "pop") == 0) {
			printf("%d\n", pop(&stack));
		}
		else if (strcmp(order_str, "size") == 0) {
			printf("%d\n", size);
		}
		else if (strcmp(order_str, "empty") == 0) {
			printf("%d\n", isEmpty(stack));
		}
		else {
			printf("%d\n", peek(stack));
		}

		free(order_str);
	}

	return 0;
}

Node* push(Node* stack, int data) {
	size++;
	Node *temp = (Node *)malloc(sizeof(Node));
	temp->data = data;
	temp->next = NULL;

	if (stack != NULL)
		temp->next = stack;

	return temp;
}
int pop(Node** stack) {
	if (*stack == NULL)
		return -1;
	else {
		size--;
		Node* temp_Node = *stack;
		*stack = (*stack)->next;

		int temp_data = temp_Node->data;
		free(temp_Node);

		return temp_data;
	}
}
int isEmpty(Node* stack) {
	if (stack == NULL)
		return 1;
	else
		return 0;
}
int peek(Node* stack) {
	if (stack == NULL)
		return -1;
	else
		return stack->data;
}