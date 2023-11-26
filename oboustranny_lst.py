class Node():
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


class ListIterator():
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()

        result = self.current.get_data()
        self.current = self.current.get_next()

        return result


class DoubleList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        return ListIterator(self.head)

    def get_size(self):
        """Return size of list"""
        return self.size

    def print_list(self):
        """Print list"""
        current = self.head

        while current is not None:
            print(current.get_data())
            current = current.get_next()

    def push(self, data):
        """Add data to the end of list"""
        temp = Node(data)

        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp

        self.size += 1

    def remove(self, data_to_remove):
        """Remove data, just once"""
        current = self.head

        while current is not None:
            if current.get_data() is data_to_remove:
                break
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Vichr z hor")

        if current is self.head:
            next_node = current.get_next()

            if next_node is not None:
                next_node.set_prev(None)
                self.head = current.get_next()
            else:
                self.head = None
                self.tail = None

        elif current is self.tail:
            prev_node = current.get_prev()
            prev_node.set_next(None)
            self.tail = prev_node

        else:
            next_node = current.get_next()
            prev_node = current.get_prev()
            next_node.set_prev(prev_node)
            prev_node.set_next(next_node)

        self.size -= 1

    def remove_symbol(self, symbol_to_remove):
        """Remove all same data you want"""
        current = self.head

        while current is not None:
            if current.get_data() is symbol_to_remove:
                if current is self.head:
                    next_node = current.get_next()

                    if next_node is not None:
                        next_node.set_prev(None)
                        self.head = current.get_next()
                    else:
                        self.head = None
                        self.tail = None

                elif current is self.tail:
                    prev_node = current.get_prev()
                    prev_node.set_next(None)
                    self.tail = prev_node

                else:
                    next_node = current.get_next()
                    prev_node = current.get_prev()
                    next_node.set_prev(prev_node)
                    prev_node.set_next(next_node)
                current = current.get_next()
                self.size -= 1
            else:
                current = current.get_next()

    def insert_after(self, input, after):
        """Add data after data of your choice"""
        current = self.head

        while current is not None:
            if current.get_data() is after:
                break
            else:
                current = current.get_next()
        # prvek tam neni
        if current is None:
            raise ValueError("Vichr z hor")
        # je to na konci
        new_node = Node(input)
        if current.get_next() is None:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node

        else:
            new_next = current.get_next()
            new_node.set_next(new_next)
            new_node.set_prev(current)

            current.set_next(new_node)
            new_next.set_prev(new_node)

        self.size += 1

    def copy(self, list_to_copy):
        """Copy list - for adding list methods"""
        current = list_to_copy.head

        while current is not None:
            self.push(current.get_data())

            current = current.get_next()

    def add_list(self, list_to_add):
        """Add the list"""
        new_list = DoubleList()
        new_list.copy(list_to_add)

        if self.head is None:
            self.head = new_list.head
            self.tail = new_list.tail

        elif new_list.head is None:
            pass

        else:
            self.tail.set_next(new_list.head)
            new_list.head.set_prev(self.tail)
            self.tail = new_list.tail

        self.size += new_list.size

    def insert_list_after(self, list_to_add, after):
        """Insert list after data of your choice"""
        insert_list = DoubleList()
        insert_list.copy(list_to_add)

        current = self.head

        while current is not None:
            if current.get_data() is after:
                break
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Vichr z  hor")

        if current.get_next() is None:
            self.add_list(insert_list)

        else:
            insert_list.tail.set_next(current.get_next())
            insert_list.head.set_prev(current)
            current.get_next().set_prev(insert_list.tail)
            current.set_next(insert_list.head)

        self.size += insert_list.size

    def insertion_sort(self):
        current = self.head

        while current is not None:
            next_node = current.get_next()

            while next_node is not None and next_node.get_prev() is not None and next_node.get_prev().get_data() > next_node.get_data():
                temp = next_node.get_data()
                next_node.set_data(next_node.get_prev().get_data())
                next_node.get_prev().set_data(temp)
                next_node = next_node.get_prev()

            current = current.get_next()

    def partition(self, left, right):
        pivot = right.get_data()
        index = left.get_prev()
        current = left

        while current != right.get_next():
            if current.get_data() <= pivot:
                if index is None:
                    index = left
                else:
                    index = index.get_next()
                temp = index.get_data()
                index.set_data(current.get_data())
                current.set_data(temp)

            current = current.get_next()

        return index

    def quick_sort(self, left, right):
        if right is not None and left != right and left != right.get_next():
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot.get_prev())
            self.quick_sort(pivot.get_next(), right)

lst = DoubleList()
lst.push(9)
lst.push(7)
lst.push(16)
lst.push(11)
lst.push(2)
lst.push(6)
lst.push(5)
lst.push(3)
lst.push(25)
lst.push(35)
lst.push(2)
lst.push(3)
lst.push(8)

lst.print_list()
print("======")
lst.quick_sort(lst.head, lst.tail)
lst.print_list()