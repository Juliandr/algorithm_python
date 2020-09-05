#This is the implementation of B_tree.
class Node:
    def __init__(self, data, par = None):
        self.data = list([data])
        self.parent = par
        self.child = list()

    def __srt__(self):
        if self.parent:
            return str(self.parent.data) + ':' + str(self.data)
        return 'Root:' +str(self.data)
    
    def __lt__(self, node):
        return self.data[0] < node.data[0]
    
    def _isLeaf(self):
        return len(self.child) == 0
    
    def _add(self, new_node):
        for data in new_node.data:
            if data in self.data:
                return False
        for child in new_node.child:
            child.parent = self
        self.data.extend(new_node.data)
        self.data.sort()
        self.child.extend(new_node.child)
        if len(self.child) > 1:
            self.child.sort()
        if len(self.data) > 2:
            self._split()
        return True
    
    def _insert(self, new_node):
        insert_done = False
        if self._isLeaf():
            insert_done = self._add(new_node)
        elif new_node.data[0] > self.data[-1]:
            insert_done = self.child[-1]._insert(new_node)
        else:
            for i in range(0, len(self.data)):
                if new_node.data[0] == self.data[i]:
                    break
                if new_node.data[0] <  self.data[i]:
                    insert_done = self.child[i]._insert(new_node)
                    break
        return insert_done
    
    def _split(self):
        left_child = Node(self.data[0], self)
        right_child = Node(self.data[2], self)
        if self.child:
            self.child[0].parent = left_child
            self.child[1].parent = left_child
            self.child[2].parent = right_child
            self.child[3].parent = right_child
            left_child.child = [self.child[0], self.child[1]]
            right_child.child = [self.child[2], self.child[3]]
        
        self.child = [left_child]
        self.child.append(right_child)
        self.data = [self.data[1]]
        
        if self.parent:
            if self in self.parent.child:
                self.parent.child.remove(self)
            self.parent._add(self)
        else:
            left_child.parent = self
            right_child.parent = self
    
    # def _find(self, item):
    #     if item in self.data:
    #         return item
    #     elif self._isLeaf():
    #         return False
    #     elif item > self.data[-1]:
    #         return self.child[-1]._find(item)
    #     else:
    #         for i in range(len(self.data)):
    #             if item <  self.data[i]:
    #                 return self.child[i]._find(item)
    





class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, item):
        insert_done = True
        if self.root is None:
            self.root = Node(item)
        else:
            insert_done = self.root._insert(Node(item))
            while self.root.parent:
                self.root = self.root.parent
        return  insert_done
    
    def find(self, item):
        return self.root._find(item)

    def remove(self, item):
        return self.root._remove(item)

    def printTop2Tiers(self):
        print(str(self.root.data))
        for child in self.root.child:
            print(str(child.data), end=' ')
            print(' ')
    
    def preorder(self):
        print('-------Preorder-------')
        self.root._preorder()
s_list = [1,2]
tree = Tree()
count = 0
for item in s_list:
	if tree.insert(int(item)):
		count += 1
print(count)
            