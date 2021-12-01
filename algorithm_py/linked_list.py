# -*- coding = utf-8 -*-

class Node(object):
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next

class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):    # O(n)
        prevnode = self.root
        curnode = self.root.next
        while curnode.next is not None:
            if curnode.value == value:
                prevnode.next = curnode.next
                del curnode
                self.length -= 1
                return

    def find(self, value):  #O(n)
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):      #O(1)
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0

def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)

    assert len(ll) == 3
    assert ll.find(2) == 2
    assert ll.find(3) == -1

    ll.remove(0)
    assert len(ll) == 2
    assert ll.find(0) == -1

    assert list(ll) == [1, 2]

    ll.appendleft(0)
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert  headvalue == 0
    assert len(ll) == 2

    ll.clear()
    assert len(ll) == 0

test_linked_list()