# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

## Class that Creates Nodes
class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None
        
# Class to define Link List 
class LinkList:
    def __init__(self):
        self.head=None
        
    def print_LL(self):
        str1="";
        if self.head==None:
            print ("LL is Empty")
        else:
                while n is not None:
                    str = str+"->"
                    print
                
    def add_to_LL(self,data):
        NN = Node(data)
        NN.next=self.head
        self.head=NN
        
L1=LinkList()
L1.add_to_LL(1);
L1.add_to_LL(2);
L1.add_to_LL(3);
L1.add_to_LL(4);
L1.print_LL()


                
                
            
            