# Linked list Deletion in Python: At beginning, End, Given location.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push_back(self, newElement):
        newNode = Node(newElement)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
    def delete_first(self):
        if self.head is not None:
            print(f"Deleted first element: {self.head.data}")
            self.head = self.head.next
        else:
            print("List is already empty.")
    def delete_last(self):
        if self.head is None:
            print("List is already empty.")
            return
        if self.head.next is None:
            print(f"Deleted last element: {self.head.data}")
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        print(f"Deleted last element: {temp.next.data}")
        temp.next = None
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty.")
            return
        if position == 0:
            print(f"Deleted element at position 0: {self.head.data}")
            self.head = self.head.next
            return
        temp = self.head
        index = 0
        prev = None
        while temp is not None and index < position:
            prev = temp
            temp = temp.next
            index += 1
        if temp is None:
            print("Position out of range.")
        else:
            print(f"Deleted element at position {position}: {temp.data}")
            prev.next = temp.next
    def PrintList(self):
        temp = self.head
        if temp is not None:
            print("The list contains:", end=" ")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")
# ---- Main Program ----
MyList = LinkedList()
print("\nMenu:")
print("1 - Add element")
print("2 - Delete first element")
print("3 - Delete last element")
print("4 - Delete element at position")
print("5 - Display list")
print("0 - Exit")
while True:
    try:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            data = int(input("Enter the element to add: "))
            MyList.push_back(data)
        elif choice == 2:
            MyList.delete_first()
        elif choice == 3:
            MyList.delete_last()
        elif choice == 4:
            position = int(input("Enter the position to delete (0-based index): "))
            MyList.delete_at_position(position)
        elif choice == 5:
            MyList.PrintList()
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid integer.")