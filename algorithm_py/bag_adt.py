# _*_ coding: utf-8 _*_

class Bag(object):
    """define a object, Bag"""
    def __init__(self, maxsize=10):
        """define a container"""
        self.maxsize = maxsize
        self._items = list()

    def add(self, item):
        """define a method, add"""
        if len(self) > self.maxsize:
            raise Exception('Bag is Full')      # if content is excess, raise an error
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2

    for i in bag:
        print(i)

test_bag()