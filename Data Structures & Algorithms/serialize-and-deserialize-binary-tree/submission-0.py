# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # root = [1,2,3,null,null,4,5]
    # [1] -> s = "1"
    # [2,null,null] -> s = "1#L-2#L-N#R-N#"
    # [3,4,5] -> s = "1#L-2#L-N#R-N#R-3#L-4#R-5#"
    # What's the difference between the include N N and the not included N N?
    # I guess we can keep track of the maxLevel where there is a number, and trim it after we are done



    # deserialize from "1#L-2#L-N#R-N#R-3#L-4#R-5"
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return "#".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split("#")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i +=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i +=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()