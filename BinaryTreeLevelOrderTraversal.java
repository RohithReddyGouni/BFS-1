/**
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
/*
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {

        List<List<Integer>> result = new ArrayList<>();
        if(root == null)
            return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> nodeElements = new ArrayList<>();
            for(int i = 0 ; i < size; i++) {
                TreeNode current = queue.poll();
                nodeElements.add(current.val);
                if(current.left != null) {
                    queue.add(current.left);
                }
                if(current.right != null) {
                    queue.add(current.right);
                }
            }
            result.add(nodeElements);
        }
        return result;

    }
}