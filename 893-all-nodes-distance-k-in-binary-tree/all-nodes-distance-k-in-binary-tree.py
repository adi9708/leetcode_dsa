# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque 
class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # graph = defaultdict(list)

        # def buildGraph(node, parent, graph):
        #     # print("node \n", node)
        #     if node:
        #         if parent:
        #             graph[node.val].append(parent.val)
        #             graph[parent.val].append(node.val)
        #             # print("graph \n", graph)
        #         # print("before left")
        #         buildGraph(node.left, node, graph)
        #         # print("before right")
        #         buildGraph(node.right, node, graph)
        
        # buildGraph(root, None, graph)
        # print(graph)
        # # Use BFS to find nodes at distance K
        # queue = deque([(target.val, 0)])
        # print(queue)
        # seen = {target.val}
        # print(seen, type(seen))
        # while queue:
        #     node, dist = queue.popleft()
        #     print(node, dist)
        #     if dist == k:
        #         return [node for node, d in queue] + [node]
        #     for neighbor in graph[node]:
        #         if neighbor not in seen:
        #             seen.add(neighbor)
        #             queue.append((neighbor, dist + 1))
        # return []


        graph = defaultdict(list)
        def buildgraph(node, parent, graph):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)

                buildgraph(node.left, node, graph)
                buildgraph(node.right, node, graph)

        buildgraph(root, None, graph)

        q = deque([(target.val, 0)])
        seen = {target.val}

        while q:
            node, distance = q.popleft()
            if distance == k:
                return [node for node, d in q] + [node]
            for neigh in graph[node]:
                if neigh not in seen:
                    q.append((neigh, distance + 1))
                    seen.add(neigh)
        return []
