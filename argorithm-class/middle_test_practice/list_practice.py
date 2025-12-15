class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

    def append(self, node):
        if node is not None:
            node.link = self.link
            self.link = node

    def popNext(self):
        nxt = self.link
        if nxt is not None:
            self.link = nxt.link
            nxt.link = None
        return nxt

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def isFull(self):
        return False

    def getNode(self, pos):
        # 음수이면 None 반환
        if pos < 0:
            return None
        ptr = self.head
        for _ in range(pos):
            if ptr is None:
                return None
            ptr = ptr.link
        return ptr

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node is None:
            return None
        return node.data

    def insert(self, pos, e):
        if pos < 0:
            raise IndexError("Invalid position")
        new = Node(e)
        if pos == 0:
            new.link = self.head
            self.head = new
            return
        before = self.getNode(pos - 1)
        if before is None:
            raise IndexError("Position out of range")
        before.append(new)

    def delete(self, pos):
        if pos < 0:
            raise IndexError("Invalid position")
        if self.head is None:
            return None
        if pos == 0:
            removed = self.head
            self.head = self.head.link
            removed.link = None
            return removed
        before = self.getNode(pos - 1)
        if before is None:
            return None
        return before.popNext()

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            count += 1
            ptr = ptr.link
        return count

    def display(self, msg='LinkedList: '):
        print(msg, end=' ')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='->')
            ptr = ptr.link
        print('None')

# ---------------------------------------------------

class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next

    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next = node

    def popNext(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
            node.next = None
            node.prev = None
        return node

class DblLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def isFull(self):
        return False

    def getNode(self, pos):
        if pos < 0:
            return None
        ptr = self.head
        for _ in range(pos):
            if ptr is None:
                return None
            ptr = ptr.next
        return ptr

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node is None:
            return None
        return node.data

    def insert(self, pos, e):
        if pos < 0:
            raise IndexError("Invalid position")
        new = DNode(e)
        if pos == 0:
            new.next = self.head
            if new.next is not None:
                new.next.prev = new
            self.head = new
            return
        before = self.getNode(pos - 1)
        if before is None:
            raise IndexError("Position out of range")
        before.append(new)

    def delete(self, pos):
        if pos < 0:
            raise IndexError("Invalid position")
        if self.head is None:
            return None
        if pos == 0:
            removed = self.head
            self.head = removed.next
            if self.head is not None:
                self.head.prev = None
            removed.next = None
            removed.prev = None
            return removed
        before = self.getNode(pos - 1)
        if before is None:
            return None
        return before.popNext()

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            count += 1
            ptr = ptr.next
        return count

    def display(self, msg='LinkedList: '):
        print(msg, end=' ')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='<->')
            ptr = ptr.next
        print('None')

# ------------------ 실행 예시 ------------------
if __name__ == "__main__":
    s = DblLinkedList()
    s.display('초기:')
    s.insert(0, 10)
    s.insert(0, 20)
    s.insert(1, 30)
    s.insert(s.size(), 40)
    s.insert(2, 50)
    s.display('연결리스트:')
    s.delete(2)
    s.delete(3)
    s.delete(0)
    s.display('마지막:')
