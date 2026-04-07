# Python Program to search an element in singly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    # Add element at the end of the list
    def push_back(self, newElement):
        newNode = Node(newElement)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
    # Search for an element
    def search(self, ele):
        temp = self.head
        pos = 1
        while temp:
            if temp.data == ele:
                print(f"{ele} is found at position = {pos}")
                return
            temp = temp.next
            pos += 1
        print(f"{ele} is not found in the linked list.")
    # Display all elements
    def show(self):
        temp = self.head
        if temp is None:
            print("The list is empty.")
        else:
            print("The list elements are:", end=" ")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()
# Main logic with improved menu
s = SinglyLinkedList()
while True:
    print("\nMenu:")
    print("1. Add element to the linked list")
    print("2. Display the linked list")
    print("3. Search for an element in the linked list")
    print("0. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == 1:
        try:
            val = int(input("Enter element to add: "))
            s.push_back(val)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == 2:
        s.show()
    elif choice == 3:
        try:
            key = int(input("Enter element to search: "))
            s.search(key)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select from the menu.")