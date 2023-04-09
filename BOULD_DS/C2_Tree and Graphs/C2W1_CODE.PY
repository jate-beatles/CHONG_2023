class Node:
    def __init__(self, key, parent = None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

        if parent != None: 
            if key < parent.key:
                assert(parent.left == None) 
                parent.left = self
            else:
                assert key > parent.key,'key is same as parent.key. We do not allow duplicate keys in BST SINCE IT BREAKS SOME OF the algorithms'
                assert(parent.right == None),'parent already has a right child -=- unable to create node'
                parent.right = self

    def get_leftmost_descendat(self):
        if self.left !=None:
            return self.left.get_leftmost_descendant()
        else: 
            return self 
                  
    def search(self,key):
        if self.key == key:
            return(True, self)
           