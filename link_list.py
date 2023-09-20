class LinkList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def addToEnd(self, data):
        node = LinkList.Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    def getFromIndex(self, index):
        while (index > 0):
            head = self.head

    def getList(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next

    def addToStart(self, data):
        node = LinkList.Node(data)
        head = self.head
        node.next = head
        self.head = node

    def addToIndex(self, index, data):
        pass

    def removeFromStart(self):
        self.head = self.head.next

    def removeFromEnd(self):
        pass

    def removeFromIndex(self, index):
        ...
        