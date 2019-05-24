# https://github.com/anrom7/Trees_easy


class LinkedBinaryTree:
    """Class for LBT representation"""
    def __init__(self, root):

        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """
        Insert to left side
        :param new_node: item
        :return:
        """
        if self.left_child is None:
            self.left_child = LinkedBinaryTree(new_node)
        else:
            t = LinkedBinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        """
        Insert to right side
        :param new_node: item
        :return:
        """
        if self.right_child is None:
            self.right_child = LinkedBinaryTree(new_node)
        else:
            t = LinkedBinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        """
        get right child of tree
        :return:
        """
        return self.right_child

    def get_left_child(self):
        """
        Get left child of tree
        :return:
        """
        return self.left_child

    def set_root_val(self, obj):
        """
        Set root
        :param obj:
        :return:
        """
        self.key = obj

    def get_root_val(self):
        """
        Get root
        :return:
        """
        return self.key

    def preorder(self):
        """
        preorder
        :return: list
        """
        lst = []
        #print(self.key)
        if self.left_child:
            lst.append(self.left_child.preorder())
        if self.right_child:
            lst.append(self.right_child.preorder())
        return lst

    def inorder(self):
        """
        inorder
        :return: list
        """
        if self.left_child:
            self.left_child.inorder()
        #print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()




