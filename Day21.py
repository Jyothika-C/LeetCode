class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next
    return head

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # Find length
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Make circular
    tail.next = head

    # Optimize k
    k = k % length

    # Find new tail
    steps = length - k - 1
    new_tail = head
    for _ in range(steps):
        new_tail = new_tail.next

    # Break circle
    new_head = new_tail.next
    new_tail.next = None

    return new_head


# -------- User Input --------
arr = list(map(int, input("Enter linked list elements: ").split()))
k = int(input("Enter value of k: "))

head = create_linked_list(arr)
new_head = rotateRight(head, k)

print("Rotated List:", print_list(new_head))

#sample input  and output
# Enter linked list elements: 1 2 3 4 5
# Enter value of k: 2
# Rotated List: [4, 5, 1, 2, 3]