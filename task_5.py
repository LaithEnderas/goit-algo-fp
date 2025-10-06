import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# вузол дерева
class Node:
    def __init__(self, key, color="#7ec8ff"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# будуємо дерево з масиву купи 
def build_tree_from_heap(heap):
    if not heap:
        return None
    nodes = [Node(v) for v in heap]
    n = len(nodes)
    for i in range(n):
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < n:
            nodes[i].left = nodes[li]
        if ri < n:
            nodes[i].right = nodes[ri]
    return nodes[0]

# створюємо градієнт кольорів у 16 системі rgb від темного до світлого
def make_gradient_hex(n, base=(18, 150, 240)):
    if n <= 0:
        return []
    out = []
    for i in range(n):
        t = i / max(1, n - 1)
        r = int(base[0] + (255 - base[0]) * t)
        g = int(base[1] + (255 - base[1]) * t)
        b = int(base[2] + (255 - base[2]) * t)
        out.append(f"#{r:02x}{g:02x}{b:02x}")
    return out

# ітеративна побудова графа networkx з фіксацією позицій
def build_graph_iterative(root):
    G = nx.DiGraph()
    if root is None:
        return G, {}
    pos = {root.id: (0, 0)}
    stack = [(root, 0.0, 0.0, 1)]  # node, x, y, layer
    while stack:
        node, x, y, layer = stack.pop()
        G.add_node(node.id, label=str(node.val), color=node.color)
        if node.right:
            rx = x + 1 / (2 ** layer)
            ry = y - 1
            pos[node.right.id] = (rx, ry)
            G.add_edge(node.id, node.right.id)
            stack.append((node.right, rx, ry, layer + 1))
        if node.left:
            lx = x - 1 / (2 ** layer)
            ly = y - 1
            pos[node.left.id] = (lx, ly)
            G.add_edge(node.id, node.left.id)
            stack.append((node.left, lx, ly, layer + 1))
    return G, pos

# ітеративні обходи
def dfs_iter(root):
    if not root:
        return []
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order

def bfs_iter(root):
    if not root:
        return []
    order = []
    q = deque([root])
    while q:
        node = q.popleft()
        order.append(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return order

# фарбуємо вузли за порядком відвідування
def color_by_order(order):
    cols = make_gradient_hex(len(order))
    for node, c in zip(order, cols):
        node.color = c

# візуалізація дерева
def draw_tree(root, title):
    if root is None:
        print("дерево порожнє")
        return
    G, pos = build_graph_iterative(root)
    labels = {n: d["label"] for n, d in G.nodes(data=True)}
    colors = [d["color"] for _, d in G.nodes(data=True)]
    plt.figure(figsize=(8, 5))
    nx.draw(G, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.axis("off")
    plt.show()

# головні функції 
def visualize_dfs(heap_list):
    root = build_tree_from_heap(heap_list)
    order = dfs_iter(root)
    color_by_order(order)
    draw_tree(root, "обхід у глибину dfs")

def visualize_bfs(heap_list):
    root = build_tree_from_heap(heap_list)
    order = bfs_iter(root)
    color_by_order(order)
    draw_tree(root, "обхід у ширину bfs")

# приклад використання
if __name__ == "__main__":
    heap = [0, 4, 1, 5, 10, 3]
    print("візуалізація dfs")
    visualize_dfs(heap)
    print("візуалізація bfs")
    visualize_bfs(heap)
