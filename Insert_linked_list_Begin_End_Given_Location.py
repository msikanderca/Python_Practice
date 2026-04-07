# Insertion in linked list Python program: At Beginning, End and Given Location.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def pushFirst(self, newElement):
        newNode = Node(newElement)
        newNode.next = self.head
        self.head = newNode
    def pushAtLocation(self, newElement, position):
        newNode = Node(newElement)
        if position < 1:
            print("Position should be >= 1")
        elif position == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, position - 1):
                if temp is not None:
                    temp = temp.next
                else:
                    break
            if temp is not None:
                newNode.next = temp.next
                temp.next = newNode
            else:
                print("Position out of bounds")
    def pushLast(self, newElement):
        newNode = Node(newElement)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
# ---------------- MAIN PROGRAM ----------------
s = LinkedList()
while True:
    print("\nMenu:")
    print("1. Insert at the beginning")
    print("2. Insert at a specific position")
    print("3. Insert at the end")
    print("4. Display linked list")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        data = int(input("Enter data to insert at beginning: "))
        s.pushFirst(data)
    elif choice == '2':
        data = int(input("Enter data to insert: "))
        pos = int(input("Enter position to insert at (1-based index): "))
        s.pushAtLocation(data, pos)
    elif choice == '3':
        data = int(input("Enter data to insert at end: "))
        s.pushLast(data)
    elif choice == '4':
        print("The linked list is:")
        s.display()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select between 1-5.")