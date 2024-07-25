class node:
    def __init__(self,data):
      self.data=data    
      self.ref=None
class lin:
    def __init__(self):
        self.head=None
    def tra(self):
        if self.head is None:
            print('empty')
        else:
            n=self.head 
            while n is not None:
                print(n.data)
                
                n=n.ref
    def addbegin(self,data):
        newnode=node(data)
        newnode.ref=self.head
        self.head=newnode
        
shiv=lin()
shiv.addbegin(10)
shiv.tra()