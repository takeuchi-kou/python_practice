# -*- coding: utf-8 -*-

# 从数组和列表章复制的代码


class Array(object):

    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class Slot(object):
    """定义一个 hash 表数组的槽(slot 这里指的就是数组的一个位置)
    hash table 就是一个 数组，每个数组的元素（也叫slot槽）是一个对象，对象包含两个属性 key 和 value。
    注意，一个槽有三种状态，看你能否想明白。相比链接法解决冲突，探查法删除一个 key 的操作稍微复杂。
    1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2.使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素仍然可能是有key的，需要继续查找
    3.槽正在使用 Slot 节点
    """

    def __init__(self,key, value):
        self.key, self.value = key, value


class HashTable(object):
    UNUSED = None # slot 没被使用过
    EMPTY = Slot(None, None) # 使用过被删除

    def __init__(self):
        self.table = Array(8, init=HashTable.UNUSED)
        self.length = 0

    @property
    def _load_factor(self):
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

    def _hash(self,key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self,key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index*5 + 1) % _len  # cpython 使用的一种解决哈希冲突的方法
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index*5 +1) %_len
        return None

    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or self._talbe[index] is HashTable.UNUSED)

    def _find_slot_for_insert(self,key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index*5 + 1) % _len
        return index