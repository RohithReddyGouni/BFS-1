# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        Que=deque([root]);
        result=[];
        while Que:
            length=len(Que);
            rightSide=None;
            for i in range(length):
                node=Que.popleft();
                if node:
                    rightSide=node;
                    Que.append(rightSide.left);
                    Que.append(rightSide.right);
                
            if rightSide:
                result.append(rightSide.val);
        return result;