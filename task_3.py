import heapq
from collections import defaultdict

# граф як словник суміжності
# graph[u] -> список пар (v, w) де w це вага ребра u->v
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v, w, undirected=False):
        # додаємо ребро з вагою
        self.adj[u].append((v, w))
        if undirected:
            self.adj[v].append((u, w))

def dijkstra(graph, start):
    # ініціалізація
    dist = {v: float("inf") for v in graph.adj}
    # важливо додати вершини які зʼявляються лише як кінцеві
    for u in list(graph.adj):
        for v, _ in graph.adj[u]:
            if v not in dist:
                dist[v] = float("inf")

    dist[start] = 0
    parent = {start: None}
    heap = [(0, start)]  # пари (відстань, вершина)

    # основний цикл алгоритму
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue  # пропускаємо застарілий запис
        for v, w in graph.adj.get(u, []):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(heap, (nd, v))
    return dist, parent

def reconstruct_path(parent, start, target):
    # відновлення шляху з target до start
    if target not in parent and target != start:
        return []
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()
    return path

# приклад використання
if __name__ == "__main__":
    g = Graph()
    # створюємо зважений граф
    g.add_edge("A", "B", 4, undirected=True)
    g.add_edge("A", "C", 2, undirected=True)
    g.add_edge("B", "C", 5, undirected=True)
    g.add_edge("B", "D", 10, undirected=True)
    g.add_edge("C", "E", 3, undirected=True)
    g.add_edge("E", "D", 4, undirected=True)
    g.add_edge("D", "F", 11, undirected=True)

    start = "A"
    dist, parent = dijkstra(g, start)

    print(f"найкоротші відстані від {start}")
    for v in sorted(dist):
        print(v, dist[v])

    target = "F"
    path = reconstruct_path(parent, start, target)
    print(f"шлях від {start} до {target} {path}")
