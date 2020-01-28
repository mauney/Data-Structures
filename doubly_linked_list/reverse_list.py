class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def add(self, value):
        self.next = Node(value)


def reverse_list(head):
    """reverses a singly-linked-list and returns the new head node"""
    # remember original head as it moves down the list
    pivot = head
    # if two more items exist after the pivot...
    while pivot.next and pivot.next.next:
        # remember the second and move the first to the head
        temp = pivot.next.next
        pivot.next.next = head
        head = pivot.next
        # join the pivot to the second
        pivot.next = temp
    # for the last item:
    temp.next = head
    pivot.next = None
    head = temp
    return head


values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# start a linked list with the first value
original_head = Node(values[0])
# keep track of the last item
tail = original_head
# add a list item for each remaining value and update tail to end of list
for value in values[1:]:
    tail.add(value)
    tail = tail.next

# test that we have a linked list
# create a pointer to the head of the list
walk = original_head
# grab the first value
original_order = [walk.value]
# as long as there is a next item, move there and add it's value
while walk.next:
    walk = walk.next
    original_order.append(walk.value)
    
print(original_order)

# moment of truth
new_head = reverse_list(original_head)

# test that we have a reversed linked list
walk = new_head
# grab the first value
new_order = [walk.value]
# as long as there is a next item, move there and add it's value
while walk.next:
    walk = walk.next
    new_order.append(walk.value)
    
print(new_order)