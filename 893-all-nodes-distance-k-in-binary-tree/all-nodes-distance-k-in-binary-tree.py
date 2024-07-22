# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        _dict = {}
        self.buildgraph(root, None, _dict)
        q = [(target, 0)]

        visited = set([target])
        res = []

        while q:
            node, dist = q.pop(0)
            if dist == k:
                res.append(node.val)

            if dist > k:
                break

            for neigh in _dict[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append((neigh, dist + 1))
        
        return res
        
    def buildgraph(self, node, parent, _dict):
        if not node: return 

        if node not in _dict: 
            _dict[node] = []

        if parent:
            _dict[node].append(parent)
            _dict[parent].append(node)
        







        
        self.buildgraph(node.left, node, _dict)
        self.buildgraph(node.right, node, _dict)

        