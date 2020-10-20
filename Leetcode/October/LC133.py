def main():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.neighbors = [two, four]
    two.neighbors = [three, four]
    three.neighbors = [two, four]
    four.neighbors = [one, three]
    print(Solution.cloneGraph(Solution,one).neighbors)


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        nodeCopy = Node(node.val)
        dict = {node: nodeCopy}
        self.dfs(self, node, dict)
        return dict[node]

    def dfs(self, node, dict):
        for neighbor in node.neighbors:
            if neighbor not in dict:
                neighbor_copy = Node(neighbor.val)
                dict[neighbor] = neighbor_copy
                self.dfs(self, neighbor, dict)
            dict[node].neighbors.append(dict[neighbor])


if __name__ == "__main__":
    main()
