from node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)

        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size += 1

    def pop(self):
        if self.first is not None:
            elem = self.first.data
            self.first = self.first.next

            self._size -= 1
            return elem

        raise IndexError("The Queue is Empty")

    def peak(self):
        if self.first is not None:
            elem = self.first.data
            return elem

        raise IndexError("The Queue is Empty")

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while pointer:
                r += str(pointer.data.processName) + " | "
                pointer = pointer.next
            return r
        return " "

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, item):
        pointer = self.first
        for i in range(item):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")

        if pointer:
            return pointer.data
        raise IndexError("List index out of range")

    def exists(self, elem):
        if self.first:
            pointer = self.first

            while pointer:
                if pointer.data.processName == elem:
                    return True
                pointer = pointer.next

            return False
        else:
            print("Fila Vazia!")
            return False
