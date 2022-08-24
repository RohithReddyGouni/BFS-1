# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        Que=deque();
        Que.append(root)
        if not root:
            return [];
        result=[];
        
        while Que:
            temp=[];
            Tree=len(Que);
            for _ in range(Tree):
                node=Que.popleft();
                if node.left:
                    Que.append(node.left);
                if node.right:
                    Que.append(node.right);
                temp.append(node.val);
            result.append(temp);
        return result;