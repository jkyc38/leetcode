import matplotlib
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
    
def printList(head):
  ptr = head
  while(ptr):
      print(f'{ptr.val} ->', end=" ")
      ptr = ptr.next
  print("None")
# 3->4->5
# 3<-4<-5
def reverseList(head):
  # Initialize three pointers
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # Save the next node
        curr.next = prev       # Reverse the current node's pointer
        prev = curr            # Move prev to the current node
        curr = next_node       # Move curr to the next node

    return prev  # prev will be the new head of the reversed list


def middleList(head):
  #two pointers
  #both initialized at the beginning of the list
  #fast traverses two nodes while the slow traverses one
  first = head
  second = head

  while second and second.next:
     first = first.next
     second = second.next.next
  # print(first.val)
  return first.val


def init_list(num):
  
  head = LinkedList(0)
  ptr = head
  for i in range(1,num):
    ptr.next = LinkedList(i)
    ptr = ptr.next

  return head

def mergeTwoLists(list1, list2):
    #you can make a dummy list
    #init linkedlist
    dummy = LinkedList()
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
            
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    if list1:
       curr.next = list1
    
    elif list2:
       curr.next = list2
    
    return dummy.next
def hasCycle(head):
        init = set()
        while head:
            if head in init:
                return True
            init.add(head)
            head = head.next #traverse list

        return False

def hasCycle(head):
	slow, fast = head, head


      
l1 = init_list(4)
l2 = init_list(2)
l3 = mergeTwoLists(l1, l2)
printList(l3)

from typing import Optional
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    count = 0
    fast = head
    curr = head
    prev = None
    while count<n:
        fast = fast.next
        count+=1
    if not fast:
        return head.next
    while fast:
        prev = curr
        curr = curr.next
        fast = fast.next
    
    prev.next = prev.next.next #delete the node

    return head


        