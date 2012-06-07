#!/usr/bin/env python3

class AVLTree(object):
    def __init__(self, value):
        self.tree = [value, None, None]

    def insert(self, item):
        root = self.tree
        value, left, right = self.tree
        child = self.__class__(item)
        while True:
            if value < item:
                if left is not None:
                    root = left.tree
                    value, left, right = root
                else:
                    root[1] = child
                    break
            elif value > item:
                if right is not None:
                    root = right.tree
                    value, left, right = root
                else:
                    root[2] = child
                    break
        balance_factor = self.balance_factor()

    def height(self):
        left, right = self.tree[1], self.tree[2]
        if left is None:
            if right is None:
                return 1
            return right.height() + 1
        elif right is None:
            if left is None:
                return 1
            return left.height() + 1
        return max(right.height(), left.height()) + 1

    def balance_factor(self):
        value, left, right = self.tree
        left_height = 0 if left is None else left.height() 
        right_height = 0 if right is None else right.height() 
        return left_height - right_height

    def __repr__(self):
        return '({}, {}, {})'.format(*self.tree)
