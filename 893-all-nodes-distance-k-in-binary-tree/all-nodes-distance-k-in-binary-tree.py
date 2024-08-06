# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def buildGraph(node, parent, graph):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                buildGraph(node.left, node, graph)
                buildGraph(node.right, node, graph)
        
        buildGraph(root, None, graph)

        # Use BFS to find nodes at distance K
        queue = deque([(target.val, 0)])
        seen = {target.val}
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                return [node for node, d in queue] + [node]
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return []