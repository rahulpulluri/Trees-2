from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # For printing the tree in level-order
    def __repr__(self):
        result = []
        queue = [self]
        while any(queue):
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        # Trim trailing "null"s
        while result and result[-1] == "null":
            result.pop()
        return "[" + ",".join(result) + "]"

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        indices = {}

        for idx, val in enumerate(inorder):
            indices[val] = idx

        self.post_idx = len(postorder) - 1

        def dfs(l, r):
            
            if l > r:
                return None
            
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            idx = indices[root_val]

            
            root.right = dfs(idx + 1, r)
            root.left = dfs(l,idx-1)

            return root


        return dfs(0, len(inorder)-1)

        
        
        # Brute Force Recursive Approach
        # if not inorder or not postorder:
        #     return None

        # root_val = postorder[-1]
        # root = TreeNode(root_val)

        # mid = inorder.index(root_val)

        # # Recursive calls (with slicing, which is O(n) each)
        # root.left = self.buildTree(inorder[:mid], postorder[:mid])
        # root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])

        # return root

if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    sol = Solution()
    root = sol.buildTree(inorder, postorder)

    print("Constructed Binary Tree:", root)
