#SLL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def front(self):
        print(self.head.data)
        return self.head.data

    def addFront(self, val):
        new_node = Node(val)
        if self.head != None:
            new_node.next = self.head
        self.head = new_node
        return self

    def removeFront(self):
        current_node = self.head
        if current_node != None:
            self.head = current_node.next
        return self

    def contains(self, val):
        looking_for = val
        current_node = self.head
        while current_node != None:
            if current_node.data == looking_for:
                print(current_node.data)
                return True
            current_node = current_node.next
        return False

    def length(self):
        runner = self.head
        length = 0
        while runner != None:
            length += 1
            runner = runner.next
        print(length)
        return length

    def display(self):
        runner = self.head
        all_items = ""
        while runner != None:
            all_items = all_items + str(runner.data)
            runner = runner.next
        print(all_items)
        return all_items

