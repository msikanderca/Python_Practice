# Find middle element of a linked list in single pass.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        """Add element at the beginning"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def pushLast(self, new_data):
        """Add element at the end"""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def findMiddle(self):
        """Find the middle element using single pass (two-pointer approach)"""
        slow = self.head
        fast = self.head

        # Traverse the list with fast pointer moving twice as fast as slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle element is:", slow.data)
        else:
            print("The list is empty.")

    def __str__(self):
        """Return string representation of the list"""
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        return " -> ".join(result) if result else "[Empty List]"


# Main program
s = SinglyLinkedList()

print("Linked List Menu:")
print("1: Add element at the beginning")
print("2: Add element at the end")
print("3: Find middle element")
print("4: Display the linked list")
print("0: Exit")

while True:
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("[INVALID INPUT]: Please enter a valid number.")
        continue

    if choice == 0:
        print("Exiting program.")
        break
    elif choice == 1:
        data = input("Enter element to add at beginning: ")
        s.push(data)
    elif choice == 2:
        data = input("Enter element to add at end: ")
        s.pushLast(data)
    elif choice == 3:
        s.findMiddle()
    elif choice == 4:
        print("Linked list contents:")
        print(s)
    else:
        print("[INVALID INPUT]: Please enter a valid menu option.")