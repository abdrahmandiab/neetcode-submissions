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
        if not root:
            return "N"
        res = []
        queue = deque([root])
        while queue:
            node= queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        x = "#".join(res)
        #print(x) returns #1#2#3#N#N#4#5#N#N#N#N 
        return x
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split("#")
        if vals[0]=="N":
            return None
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index+=1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index+=1
        return root
        