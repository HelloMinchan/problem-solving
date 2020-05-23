/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode *make_tree(int *arr, int p, int r) {
    if(p > r)
        return NULL;
    else {
        struct TreeNode *tree_head = (struct TreeNode *)malloc(sizeof(struct TreeNode));
        int q = (p+r)/2;
    
        tree_head->val = arr[q];
        tree_head->left = make_tree(arr, p, q-1);
        tree_head->right = make_tree(arr, q+1, r);
    
        return tree_head;
    }
}
struct TreeNode* sortedListToBST(struct ListNode* head){
    int len = 0;
    struct ListNode *cur = head;
    while(cur!=NULL) {
        len++;
        cur=cur->next;
    }
    
    int *arr = (int *)malloc(sizeof(int)*len);
    int i = 0;
    cur = head;
    while(cur!=NULL) {
        arr[i++]=cur->val;
        cur=cur->next;
    }
    
    struct TreeNode *tree_head = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    tree_head = make_tree(arr, 0, len-1);
    
    free(arr);
    return tree_head;
}
