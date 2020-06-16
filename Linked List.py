class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head == None:
            node = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data,itr.next)
        itr.next = node

    def delete_at_beg(self):
        if self.head == None:
            print("Linked list is empty")
            return
        itr = self.head
        self.head = itr.next

    def delete_at_end(self):
        if self.head == None:
            print("Linked List is empty")
            return
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_values(self,values):
        for data in values:
            self.insert_at_end(data)

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.insert_at_beg(data)
            return
        
        count = 0
        itr = self.head
        while True:
            if(count==index-1):
                temp = itr.next
                node = Node(data,temp)
                itr.next = node
                return
            itr = itr.next
            count += 1

    def delete_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Exception")
        if index==0:
            self.delete_at_beg()
            return
        itr = self.head
        count = 0
        while True:
            if count==index-1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_after_value(self,value,data):
        itr = self.head
        while itr:
            if itr.data==value:
                node = Node(data,itr.next)
                itr.next = node
                return
            itr = itr.next
        print("Value not found")
        return

    def remove_by_value(self,value):
        itr = self.head
        if self.head==None:
            return
        if self.head.data==value:
            self.head = self.head.next
            return
        
        while itr.next:
            if itr.next.data==value:
                itr.next = itr.next.next
                return
            itr = itr.next
                

    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return
        itr = self.head
        while itr:
            print(itr.data,"->",end='')
            itr = itr.next
            

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beg(10)
    ll.insert_at_beg(5)
    ll.insert_at_end(15)
    ll.insert_at_end(20)
    ll.insert_at_end(25)
    ll.delete_at_beg()
    ll.insert_values(['A','B','C','D'])
    ll.delete_at_end()
    ll.insert_at(7,'New')
    ll.delete_at(7)
    ll.insert_at(0,5)
    ll.delete_at(0)
    ll.insert_after_value('C','D')
    ll.remove_by_value(25)
    ll.insert_after_value(20,25)
    print("Lengtb of the linked list: ",ll.get_length())
    ll.print()
