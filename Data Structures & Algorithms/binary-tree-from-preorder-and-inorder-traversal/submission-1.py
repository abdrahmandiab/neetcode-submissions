# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(val=preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


# preorder = [1,2,3,4], inorder = [2,1,3,4]
# first node of preorder is always the root
# start the tree off with that node, None is the base case if preorder or inorder are []
# Then we go to the index of the root in inorder (mid == 1)
# we split the Left SubTree and RightSubTrees from there
# for the example above:
#   LST = [2]  , RST = [3,4]
#   since we already considered the root,
#   The partition for LST in preorder is actually [1:mid+1]
#.     and the partition of LST in inorder is then.. [start:mid] -> [:mid]
#   The partition for RST in preorder is then [mid+1:end] -> [mid+1:]
#.     and finally the partition of RST in inorder is [mid+1:end] -> [mid+1:]