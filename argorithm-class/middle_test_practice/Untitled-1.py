# class ArrayStack:
#     def __init__(self. capacity):
#         self.capacity = capacity
#         self.array = [None]*self.capacity
#         self.top = -1

#     def isFull(self):
#         return self.top == self.capacity - 1
    
#     def isEmpty(self):
#         return self.top == -1
    
#     def push(self. item):
#         if not self.isFull():
#             self.top += 1
#             self.array[self.top] = item

#     def pop(self):
#         if not self.isEmpty():
#             self.top -= 1
#             item = self.array[self.top]
#             self.array[self.top] = None
#             return item
        
#     def peek(self):
#         if not self.isEmpty():
#             return self.array[self.top]
#         return None
    
#     def size(self):
#         return self.top + 1

# class ArrayStack:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.array = [None]*self.capacity
#         self.top = -1

#     def isFull(self):
#         return self.top == self.capacity - 1
    
#     def isEmpty(self):
#         return self.top == -1
    
#     def push(self, item):
#         if not self.isFull():
#             self.top += 1
#             self.array[self.top] = item

#     def pop(self):
#         if not self.isEmpty():
#             self.top -= 1
#             item = self.array[self.top]
#             self.array[self.top] = None
#             return item
    
#     def peek(self):
#         if not self.isEmpty():
#             return self.array[self.top]
#         return None
        
#     def size(self):
#         return self.top + 1

    # def reverse_string(statement: str) -> str:
    # print("\n[1] PUSH 단계 -----------------")
    # st = ArrayStack(len(statement))
    # for ch in statement:
    #     st.push(ch)

    # print("\n[2] POP 단계 ------------------")
    # out = []
    # while not st.is_empty():
    #     out.append(st.pop())

    # result = ''.join(out)
    # print(f"\n[3] 최종 결과: {result}")
    # return result

# s = ArrayStack(1000)

# msg = input("입력:")
# for c in msg:
#     s.push(c)

# print("출력:", end=' ')
# while not s.isEmpty():
#     print(s.pop(), end=' ')
# print()

# def factorial_iter(n):
#     result = 1
#     for k in range(2, n+1):
#         result *= k
#     return result

# def factorial_rec(n):
#     if n==1: return 1
#     else:
#         result = n * factorial_rec(n-1)
#     return result

# def factorial_iter(n):
#     result = 1
#     for k in range(2, n+1):
#         result *= k
#     return result

# def factorial_rec(n):
#     if n == 1:
#         return 1
#     else:
#         result = n * factorial_rec(n-1)
#     return result


# class ArrayQueue:
#     def __init__(self. capacity=10):
#         self.capacity = capacity
#         self.N = self.capacity + 1
#         self.array = [None] * self.capacity
#         self.rear = 0
#         self.front = 0

#     def isFull(self):
#         return self.front == (self.rear + 1) % self.N
    
#     def isEmpty(self):
#         return self.front == self.rear
    
#     def enqueue(self, item):
#         if not self.isFull():
#             self.rear = (self.rear + 1) % self.N
#             self.array[self.rear] = item

#     def dequeue(self):
#         if not self.isEmpty():
#             self.front = (self.front + 1)% self.N
#             item = self.array[self.front]
#             self.array[self.front] = None
#             return item
        
#     def peek(self):
#         if not self.isEmpty():
#             return self.array[(self.front + 1) % self.N]
#         return None
        
#     def size(self):
#         return (self.rear - self.front + self.N) % self.N

    
# class RingBuffer:
#     def __init__(self, capacity):
#         q = ArrayQueue(capacity)
#         def isEmpty(self):
#             return self.q.isEmpty()
#         def isFull(self):
#             return self.q.isFull()
        
#     def enqueue2(self, item):
#         q = self.q
#         q.rear = (q.rear + 1) % q.N
#         if q.rear == q.front:
#             q.front = (q.front + 1) % q.N
#         q.array[q.rear] = item

#     def enqueue2(self, item):
#         q= self.q
#         q.rear = (q.rear + 1) % q.N
#         if q.rear == q.front:
#             q.front = (q.front + 1) %q.N
#         q.array[q.rear] = item

#     def dequeue(self):
#         return self.q.dequeue()
#     def peek(self):
#         return self.q.peek()
#     def size(self):
#         return self.q.size()


# from circular_queue_class import CircularQueueOneSlotEmpty

# class CircularDeque(CircularQueueOneSlotEmpty):
#     def __init__(self,capacity):
#         super().__init__(capacity)

#     def addRear(self. item):
#         return self.enqueue(item)
    
#     def getFront(self):
#         return self.peek()
    
#     def deleteFront(self):
#         return self.dequeue()
    
#     def get_Front(self):
#         if not self.isEmpty():
#             return self.array[self.rear]
        
#     def add_front(self,item): #전단에서 삽입
#         if self.is_full():
#             raise IndexError("덱이 포화 상태 -> 삽입 불가")
#         else:
#             self.array[self.front]=item
#             self.front =(self.front -1) %self.N #front 를 반시계 반향으로 한 칸 회전

#     def delete_rear(self): #후단에서 삭제
#         if self.is_empty():
#             raise ImportError("덱이 빈 상태 -> 삭제불가")
#         else:
#             item = self.array[self.rear] #rear포인터는 마지막 요소를 가리킴
#             self.array[self.rear] =None
#             self.rear = (self.rear -1 + self.N) % self.N
#             return item #반환


# class Node:
#     def __init__(self, elem, link=None):
#         self.data = self.elem
#         self.link = link

#     def append(self, new):
#         new.link = self.link
#         self.link = new

#     def popNext(self):
#         #현재 노드의 다음 노드를 리스트에서 제거하고, 그 노드를 반환
#         deleted = self.link
#         if deleted is not None:
#             self.link = deleted.link
#             deleted.link = None #연결 해제 
#         return deleted

# class Node:
#     def __init__(self, elem, link=None):
#         self.data = self.elem
#         self.link = link

#     def append(self, new):
#         new.link = self.link
#         self.link = new

#     def popNext(self):
#         deleted = self.link
#         if deleted is not None:
#             self.link = deleted.link
#             deleted.link = None
#         return deleted
    
"""
1. 단순 연결 리스트 구조를 관리하는 클래스
2. head: 리스트의 첫 번째 노드를 가리키는 포인터
3. 주요 메서드:
   - isEmpty(): 리스트가 비어있는지 확인
   - isFull(): 리스트가 가득 찼는지 확인
   - getNode(pos): 특정 위치의 노드를 반환
   - getEntry(pos): 특정 위치의 노드 데이터를 반환
   - replace(pos, elem): 특정 위치의 노드 데이터를 변경
   - size(): 리스트의 크기를 반환
   - display(msg): 리스트의 내용을 출력
   - insert(pos, elem): 특정 위치에 새 노드를 삽입
   - delete(pos): 특정 위치의 노드를 삭제
   - find(elem): 특정 데이터를 가진 노드를 검색
"""
# 단순연결리스트 클래스
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def isEmpty(self):
#         #리스트가 비어있는지 검사
#         return self.head == None
    
#     def isFull(self):
#         #리스트의 포화상태 검사
#         return False
    
#     def getNode(self, pos):
#         #pos번째에 있는 노드를 반환하기
#         #리스트의 인덱스는 0부터 시작
#         if pos < 0: return None #pos는 invailed 경우
#         if self.head == None: #주어진 리스트가 공백
#             return None
#         else:
#             ptr = self.head
#             for _ in range(pos):
#                 if ptr == None: #pos가 리스트 크기보다 큰 경우
#                     return None
#                 ptr = ptr.link #링크 따라 이동
#             return ptr
        
#     def getEntry(self, pos):
#         #리스트의 pos 위치에 있는 노드의 데이터를 반환
#         node = self.getNode(pos) #getNode()를 이용하여 pos 위치에 있는 노드 먼저 찾기
#         if node == None:
#             return None
#         else:
#             return node.data
        
#     def insert(self, pos, elem):
#         #리스트의 pos 위치에 새로운 노드를 추가
#         if pos < 0: return #잦동으로 유효하지않는 위치에 대해 ValueError 발생
#         new = Node(elem, None) #또는 Node(elem)ㅡㅡ>새 노드 생성
#         before = self.getNode(pos - 1)
#         if before is None:
#             if pos == 0:
#                 new.link = self.head
#                 self.head = new
#                 return
#             else: #2)pos가 리스트의 범위를 벗어나는 경우
#                 raise IndexError("리스트 밖에 있는 위치")
#         else: #3)중간노드로 삽입
#             before.append(new) #before 노드 뒤에 삽입

#     def delete(self, pos):
#         if pos < 0:
#             raise IndexError("empty 또는 리스트 범위 밖 오류")

#         before = self.getNode(pos - 1)
#         if before == None:
#             if pos == 0:
#                 deleted = self.head
#                 self.head = deleted.link
#                 deleted.link = None
#                 return deleted
#             else:
#                 raise ValueError("리스트 범위 밖 오류")
#         else:
#             before.popNext()

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def isEmpty(self):
#         return self.head == None
#     def isFull(self):
#         return False
#     def getNode(self, pos):
#         if pos < 0: return None
#         if self.head == None:
#             return None
#         else:
#             ptr = self.head
#             for _ in range(pos):
#                 if ptr == None:
#                     return None
#                 ptr = ptr.link
#             return ptr
#     def getEntry(self. pos):
#         node = self.getNode(pos)
#         if node == None:
#             return None
#         else:
#             return node.data
#     def insert(self, pos, elem):
#         if pos < 0: return
#         new = Node(elem, None)
#         before = self.getNode(pos -1)
#         if before is None:
#             if pos == 0:
#                 new.link = self.head
#                 self.head = new
#                 return
#         else: before.append(new)
#     def delete(self, pos):
#         if pos < 0: raise IndexError
#         before = self.getNode(pos-1)
#         if before is None:
#             if pos == 0:
#                 deleted = self.head
#                 self.head = deleted.link
#                 deleted.link = None
#                 return deleted
#             else: raise ValueError
#         else: before.popNext()
#     def size(self):
#         if self.head == None:
#             return 0
#         else:
#             ptr = self.head
#             count = 0
#             while ptr is not None:
#                 count += 1
#                 ptr = ptr.link
#             return count
#     def replace(self, pos, elem):
#         node = self.getNode(pos)
#         if node is not None:
#             node.data == elem
#         else: return
# class DNode:
#     def __init__(self, elem, prev=None,next=None):
#       self.data = elem
#       self.next = next
#       self.prev = prev

#     def append(self, new):
#       #현재 노드(self) 다음에 새 노드(new)를 붙임
#       if new is not None:
#          new.next = self.next
#          new.prev = self
#          if new.next is not None:
#             new.next.prev = new
#          self.next = new

#     def popNext(self):
#        deleted = self.next
#        if deleted is not None:
#           self.next = deleted.next
#           deleted.next = None
#           if self.next is not None:
#              self.next.prev = self
#        return deleted
"""
1. 이중 연결 리스트 구조를 관리하는 클래스
2. head: 리스트의 첫 번째 노드를 가리키는 포인터
3. tail: 리스트의 마지막 노드를 가리키는 포인터(option)
4. 주요 메서드: 
    - 동일 연산
        - isEmpty(): 리스트가 비어있는지 확인 
        - isFull(): 리스트가 가득 찼는지 확인
        - getEntry(pos): 특정 위치의 노드 데이터를 반환
    - 연산에서 .link -> .next로 수정
        - getNode(pos): 특정 위치의 노드를 반환 
        - size(): 리스트의 크기를 반환
        - display(msg): 리스트의 내용을 출력
    - 나머지 연산       
        - insert(pos, elem): 특정 위치에 새 노드를 삽입
        - delete(pos): 특정 위치의 노드를 삭제
        - replace(pos, elem): 특정 위치의 노드 데이터를 변경
        - find(elem): 특정 데이터를 가진 노드를 검색
"""
# class DLinkedList:                       
#     def __init__( self ):             
#       self.head = None                
# class DLinkedList:
#     def __init__(self):
#         self.head = None
#     def isEmpty(self):
#         return self.head == None
#     def isFull(self):
#         return False    
#     def getEntry(self, pos):
#         node = self.getNode(pos)
#         if node == None:
#             return None
#         else:
#             return node.data
#     def replace(self, pos, elem):
#         node = self.getNode(pos)
#         if node != None:
#             node.data = elem
#         else:
#             return
#     def getNode(self, pos):
#         if pos < 0:
#             return None
#         if self.head == None: return None
#         else:
#             ptr = self.head
#             for _ in range(pos):
#                 if ptr == None:
#                     return None
#                 ptr = ptr.next
#             return ptr
#     def size(self):
#         if self.head == None:
#             return 0
#         else:
#             ptr = self.head
#             count = 0
#             while ptr is not None:
#                 count += 1
#                 ptr = ptr.next
#             return count
#     def insert(self, pos, elem):
#         if pos<0: return
#         new = DNode(elem):
#         before = self.getNode(pos -1)
#         if bofore == None:
#             if pos == 0:
#                 new.next = self.head
#                 if new.next is not None:
#                     new.next.prev = new
#                 self.head = new
#                 return
#         else:
#             before.append(new)
#     def delete(self, pos):
#         if pos<0: return
#         before = self.getNode(pos-1)
#         if before == None:
#             if pos == 0:
#                 deleted = self.head
#                 if self.head is not None:
#                     self.head = deleted.next
#                     self.head.prev = None
#                     deleted.prev = None
#                     deleted.next = None
#                 return deleted
#             else:
#                 return
#         else: before.popNext()