# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Time limit reached with  this approach. Use a hashmap to get O(n)
        #if not preorder or not inorder:
        #    return None
        
        #root = TreeNode(preorder[0])
        #mid = inorder.index(preorder[0])
        #root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        #root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        #return root

        indices = {val:idx for idx,val in enumerate(inorder)}

        self.preorder_index = 0
        def dfs(l,r):
            if l>r:
                return None

            root_val = preorder[self.preorder_index]
            self.preorder_index += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)

            return root

        return dfs(0, len(inorder)-1)

