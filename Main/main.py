from Core.BinaryTree.BinaryTreeVisualizer import *
from Core.BinaryTree.BinaryTree import *


def executeBinaryTree():
    bt = BinaryTree()
    bt.populateTree(7)
    print(bt.inorderRecursivo(bt.root))
    btVisualizer = BinaryTreeVisualizer(bt)
    btVisualizer.render()


if __name__ == "__main__":
    executeBinaryTree()