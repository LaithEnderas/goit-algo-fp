import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# вузол дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # колір вузла
        self.id = str(uuid.uuid4())  # унікальний ідентифікатор

# рекурсивне додавання ребер і позицій
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.val))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

# побудова дерева з масиву купи
def heap_to_tree(heap_list):
    # перетворюємо масив купи у дерево вузлів
    if not heap_list:
        return None
    nodes = [Node(v) for v in heap_list]
    n = len(nodes)
    for i in range(n):
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < n:
            nodes[i].left = nodes[li]
        if ri < n:
            nodes[i].right = nodes[ri]
    return nodes[0]

# візуалізація дерева
def draw_tree(tree_root):
    if tree_root is None:
        print("дерево порожнє")
        return
    G = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(G, tree_root, pos)
    colors = [d["color"] for _, d in G.nodes(data=True)]
    labels = {n: d["label"] for n, d in G.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(G, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.axis("off")
    plt.show()

# головна функція візуалізації бінарної купи
def visualize_heap(heap_list):
    # приймає список що представляє купу і будує з нього дерево
    root = heap_to_tree(heap_list)
    draw_tree(root)

# приклад використання
if __name__ == "__main__":
    data = [7, 3, 9, 1, 5, 8, 10]
    heap = data[:]           # копія даних
    heapq.heapify(heap)      # будуємо мін купу
    print("купа як масив", heap)
    visualize_heap(heap)     # візуалізація купи
