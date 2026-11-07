class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        if(index<self.size):
            current = self.head
            
            for i in range(0,index):
                current = current.next
            return current.val
        else:
            return -1
    def insertHead(self, val: int) -> None:
        new_head = ListNode(val,self.head)
        self.head = new_head
        self.size+=1

    def insertTail(self, val: int) -> None:
        if(self.size == 0):
            self.insertHead(val)
        else:
            new_tail = ListNode(val)
            current_tail = self.head
            for i in range(0,self.size-1):
                current_tail = current_tail.next
            current_tail.next = new_tail
            self.size+=1

    def remove(self, index: int) -> bool:
        if(index<self.size):
            if(index == self.size-1):
                previous_index_node = self.head
                for i in range(0,index):
                    previous_index_node = previous_index_node.next
                previous_index_node.next = None
            elif(index == 0):
                self.head = self.head.next
            else:
                previous_node = self.head
                current_node = self.head
                for i in range(0,index):
                    previous_node = current_node
                    current_node = current_node.next
                previous_node.next = current_node.next
            self.size-=1
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        current = self.head
        
        staticList = []
        for i in range(0,self.size):
            staticList.append(current.val)
            current = current.next
        return staticList
        
