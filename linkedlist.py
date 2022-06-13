class Node:
    def __init__(self, value=None,next=None):
        self.item = value
        self.next = next

    def __repr__(self):
        return f'Node("{self.item}","{self.next}")'

class LinkedList:
    def __init__(self):
        self.start_node = None

    def show_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.next

    def push(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.next = new_node

    def count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        c = 0
        while n is not None:
            c = c + 1
            n = n.next
        return c

    def find(self, x):
        if self.start_node is None:
            print("List has no element")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item",n.item,"is found")
                return True
            n = n.next
        print("item not found")
        return False

    def pop(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        n = self.start_node
        while n.next.next is not None:
            n = n.next
        print('deleting: ', n.next.item)
        n.next = None




    def unshift(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        a = self.start_node.item
        self.start_node = self.start_node.next
        return a


    def remove(self, x):
        if self.start_node is None:
            print("the list has no element")
            return

            # Deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.next
            return

        n = self.start_node
        while n.next is not None:
            if n.next.item == x:
                break
            n = n.next

        if n.next is None:
            print("the list has no element")
        else:
            n.next = n.next.next

    def first(self):
        if self.start_node is None:
            print("the list has no element")
            return
        return self.start_node.item

    def last(self):
        if self.start_node is None:
            print("the list has no element")
            return

        n = self.start_node
        while n.next.next is not None:
            n = n.next
        return n.next.item

    def get(self, index):
        if self.start_node is None:
            print("the list has no element")
            return
        get_index = []
        i = 0
        n = self.start_node
        while n is not None and i <= index:
            get_index.append(n.item)
            n = n.next
            i+=1
        return get_index[index]


if __name__=="__main__":

    new_linked_list = LinkedList()
    new_linked_list.push(5)
    new_linked_list.push(10)
    new_linked_list.push(15)
    new_linked_list.push(25)
    new_linked_list.push(35)
    new_linked_list.push(255)
    new_linked_list.push(3)
    new_linked_list.show_list()
    print("-----------------")
    print(new_linked_list.count())
    print("-----------------")
    new_linked_list.find(15)
    print("-----------------")
    print(new_linked_list.first())
    print("-----------------")
    print(new_linked_list.last())
    print("-----------------")
    print(new_linked_list.unshift())
    new_linked_list.remove(35)
    print("-----------------")
    new_linked_list.pop()
    print("-----------------")
    print(new_linked_list.get(2))
    print("-----------------")
    new_linked_list.show_list()

