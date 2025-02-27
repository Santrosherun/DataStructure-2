from Core.BinaryTree.TreeNode import *
import random
import string


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = TreeNode(value)

        if self.root == None:
            self.root = newNode
            return  # Forma de oprimizacion (Necesaria)

        current = self.root
        while True:
            if random.choice([True, False]):
                if current.left != None:  # left
                    current = current.left
                else:
                    current.left = newNode
                    return  # Forma de oprimizacion
            else:
                if current.right != None:  # right
                    current = current.right
                else:
                    current.right = newNode
                    return  # Forma de oprimizacion

    def populateTree(self, quantity: int):
        for letter in string.ascii_lowercase[0:quantity]:  # Llenar con letras
            self.insert(letter)

    def inorderRecursivo(self, node, result=None):
        if result == None:
            result = []
        if node != None:
            self.inorderRecursivo(node.left, result)
            result.append(node.value)
            self.inorderRecursivo(node.right, result)
        return result
