class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class doubly_ll:
    def __init__(self):
        self.head = None
    
    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end = "")
                n = n.nref
            
    def prtint_ll_reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.ref #type:ignore
            while n is not None:
                print(n.data, "-->", end = "")
                n = n.pref

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  
        else:
            new_node.nref = self.head #type: ignore
            self.head.pref = new_node    #type: ignore
            self.head = new_node
        
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node  #type: ignore
            new_node.pref = n  #type: ignore

    def add_after(self, data, x):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            
            if n is None:
                print("Given node is not present in LL")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n #type: ignore
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node  #type: ignore
    
    def add_before(self, data, x):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            
            if n is None:
                print("Given node is not present in LL")
            else:
                new_node = Node(data)
                new_node.nref = n #type:ignore
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node   #type: ignore
    
    def delete_begin(self):
        if self.head is None:
            print("LL is empty , can't delete the element")
            return

        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the Node")
        else:
            self.head = self.head.nref
            self.head.pref = None
        
    def delete_end(self):
        if self.head is None:
            print("LL is empty, can't delete the element")
            return
        if self.head.nref is None:
            self.head = None
            print("Linked list is empty after deleting the node")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None #type: ignore
    
    def delete_by_value(self,x):
        #LL is empty
        if self.head is None:
            print("LL is empty can't delete the element")
            return
        
        #only one node
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print("x is not present in dounbly linked list")
            return
        
        #delete the first node
        if self.head.data == x: 
            self.head = self.head.nref
            self.head.pref = None
            return
        
        #middle nodes
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref  #type:ignore
        else:
            if n.data == x:
                n.pref.nref = None  #type:ignore
            else:
                print("x is not present in the linked list")


dll = doubly_ll()
dll.add_begin(10)
dll.add_begin(20)
dll.add_end(34)
dll.add_end(22)
dll.add_after(25,22)
dll.add_before(30, 34)
dll.delete_begin()
dll.delete_end()
dll.delete_by_value(22)
dll.print_ll()
    