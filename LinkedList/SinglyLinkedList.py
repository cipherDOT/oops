

class Node(object):
    def __init__(self, value = None, next_node = None):
        self.val = value
        self.next_node = next_node

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def add_end(self, node):
        if self.head == None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next_node != None:
                current_node = current_node.next_node
            current_node.next_node = node

    def delete_index(self, index):
        traversing_index = 0
        previous_node = None
        current_node = self.head
        successor_node = current_node.next_node

        if index <= 0:
            self.head = successor_node
            return

        while traversing_index < index:
            if current_node.next_node != None:
                temp_node = current_node
                current_node = temp_node.next_node
                previous_node = temp_node
                successor_node = current_node.next_node
                traversing_index += 1
            else:
                print("List length too short")
                return
            
        del current_node
        previous_node.next_node = successor_node


    def delete_end(self):
        previous_node = None
        current_node = self.head

        if current_node == None:
            print("Deleting from Empty List!")
        
        elif current_node.next_node == None:
            self.head = None

        else:
            while current_node.next_node != None:
                temp_node = current_node
                current_node = temp_node.next_node
                previous_node = temp_node

            del current_node
            previous_node.next_node = None
        

    def display(self):
        if self.head:
            nodes = []
            current_node = self.head
            while current_node.next_node != None:
                nodes.append(current_node)
                current_node = current_node.next_node
            nodes.append(current_node)

            print('->'.join([str(node.val) for node in nodes]))
        else:
            print("Linked List is empty")

linked = SinglyLinkedList()
linked.add_end(Node(10))
linked.add_end(Node(20))
linked.add_end(Node(30))
linked.add_end(Node(40))
linked.add_end(Node(50))
linked.display()
linked.delete_index(2)
linked.display()
linked.delete_index(2)
linked.display()
linked.delete_index(0)
linked.display()
linked.delete_index(10)
linked.display()
