class TreeNode:
    
    def __init__(self, lp):
        self.lp = lp
        self.name = lp.base_lp.name
        self.parent = None
        self.child = {}
        
    def add_child(self, node):
        node.parent = self.lp
        key = node.lp.base_lp.name
        self.child[key] = node
        
    def summary(self):
        self.lp.base_lp.summary()
        for child_name in self.child:
            self.child[child_name].lp.base_lp.summary() 