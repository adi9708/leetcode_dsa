class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type node: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # print(node)

        # # Value of p
        # print(p)
        # p_val = p.val
        # # print(p_val)

        # # # Value of q
        # q_val = q.val

        # # # Start from the node node of the tree
        # # node = node

        # # # Traverse the tree
        # while node:
        #     print(node)

        #     # Value of current node or parent node.
        #     parent_val = node.val

        #     if p_val > parent_val and q_val > parent_val:    
        #         # If both p and q are greater than parent
        #         node = node.right
        #     elif p_val < parent_val and q_val < parent_val:
        #         # If both p and q are lesser than parent
        #         node = node.left
        #     else:
        #         # We have found the split point, i.e. the LCA node.
        #         return node
        p_val = p.val
        q_val = q.val
        node = root
        while node:
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
        
