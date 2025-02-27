from graphviz import Digraph


class BinaryTreeVisualizer:
    def __init__(self, tree):
        self.tree = tree
        self.dot = Digraph()

    def _add_nodes_edges(self, node):
        """Recursivamente agrega nodos y aristas al gráfico."""
        if node is None:
            return

        self.dot.node(node.value)  # Agrega el nodo actual

        if node.left:
            self.dot.edge(node.value, node.left.value)  # Conecta con el hijo izquierdo
            self._add_nodes_edges(node.left)

        if node.right:
            self.dot.edge(node.value, node.right.value)  # Conecta con el hijo derecho
            self._add_nodes_edges(node.right)

    def render(self, filename="binary_Tree"):
        """Genera y guarda la imagen del árbol binario."""
        self._add_nodes_edges(self.tree.root)
        self.dot.render(filename, format="png", cleanup=True)
        print(f"Árbol guardado como {filename}.png")