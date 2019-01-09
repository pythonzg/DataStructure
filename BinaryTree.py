"""
二叉树
"""

class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,item):
        new_node = Node(item)
        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.lchild is not None:
                queue.append(node.lchild)
            else:
                node.lchild = new_node
                return
            if node.rchild is not None:
                queue.append(node.rchild)
            else:
                node.rchild = new_node
                return

    def breadth_travel(self):
        """
        广度优先遍历
        :return:
        """
        node = self.root
        if node is None:
            return
        queue = [node]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def prev_order(self,node):
        """
        深度遍历:先序遍历
        :param node:
        :return:
        """
        if node is None:
            return
        print(node.elem,end=" ")
        self.prev_order(node.lchild)
        self.prev_order(node.rchild)

    def in_order(self,node):
        """
        深度遍历:中序遍历
        :param node:
        :return:
        """
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.elem,end=" ")
        self.in_order(node.rchild)

    def post_order(self,node):
        """
        深度遍历:后序遍历
        :param node:
        :return:
        """
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem,end=" ")

if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print()
    tree.prev_order(tree.root)
    print()
    tree.in_order(tree.root)
    print()
    tree.post_order(tree.root)
    print()