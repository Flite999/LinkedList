class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def addNode(self, val):
        newNode = Node(val)
        if self.head.val is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
            self.length += 1

    def printList(self):
        printArr = []
        if self.head.val is None:
            print("empty list")
        else:
            curr = self.head
            printArr.append(curr.val)
            while curr.next is not None:
                curr = curr.next
                printArr.append(curr.val)
        print(printArr)

    def removeNode(self, val):
        curr = self.head
        if curr.val == val:
            self.head = curr.next
        else:
            for i in range(self.length):
                prevNode = curr
                curr = curr.next
                if curr.val == val:
                    prevNode.next = curr.next
                    return
            print("No Node found by that value")
            
                


# Validation

myLL = LinkedList()
myLL.addNode(2)
myLL.addNode(3)
myLL.addNode(4)
myLL.printList()
myLL.removeNode(2)
myLL.printList()