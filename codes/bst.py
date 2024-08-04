class Binary_search_tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    
    def insert(self,value):
        if value > self.value:
            if self.right == None:
                self.right = Binary_search_tree(value)
            else:
                self.right.insert(value)
                
        if  value < self.value:
            if self.left == None:
                self.left = Binary_search_tree(value)
            else:
                self.left.insert(value)
                
    def search(self, value):
        current = self
        found = False
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True
                break
        return found
            
bst= Binary_search_tree(90)
bst.insert(50)
bst.insert(110)
bst.insert(60)
bst.insert(40)
bst.insert(115)
bst.insert(30)
bst.insert(105)
bst.insert(45)

print(bst.search(120))
print(bst.search(30))