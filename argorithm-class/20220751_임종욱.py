class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new):
        new.link = self.link
        self.link = new

    def popNext(self):
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def isFull(self):
        return False
    
    def insert(self, book):
        new_node = Node(book, self.head)
        self.head = new_node

    def find_by_title(self, title):
        node = self.head
        while node is not None:
            if node.data.title == title:
                return node.data
            node = node.link
        return None

    def find_pos_by_title(self, title):
        node = self.head
        prev = None
        while node is not None:
            if node.data.title == title:
                return prev
            prev = node
            node = node.link
        return None

    def remove(self, title):
        if self.isEmpty():
            print("등록된 도서가 없음")
            return False
        if self.head.data.title == title:
            self.head = self.head.link
            print(f"'{title}' 도서가 삭제됨")
            return True
        prev = self.find_pos_by_title(title)
        if prev is None:
            print("해당 도서가 없음")
            return False
        if prev.link is None:
            print("해당 도서가 없음")
            return False
        prev.popNext()
        print(f"'{title}' 도서가 삭제됨")
        return True

    def display_all(self):
        if self.isEmpty():
            print("현재 등록된 도서가 없음")
            return
        node = self.head
        while node is not None:
            print(node.data)
            node = node.link


class Book:
    def __init__(self, book_num, title, author, year):
        self.book_num = book_num
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[{self.book_num}] {self.title} / {self.author} / {self.year}"

class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self):
        book_num = input("책 번호: ")
        title = input("책 제목: ")
        author = input("저자: ")
        year = input("출판 연도: ")
        node = self.books.head
        while node is not None:
            if node.data.book_id == book_num or node.data.title == title:
                print("동일한 책 번호 또는 제목이 이미 존재함")
                return
            node = node.link

        new_book = Book(book_num, title, author, year)
        self.books.insert(new_book)
        print(f"'{title}' 도서가 추가됨")

    def remove_book(self):
        title = input("삭제할 책 제목: ")
        self.books.remove(title)

    def search_book(self):
        title = input("조회할 책 제목: ")
        book = self.books.find_by_title(title)
        if book:
            print(book)
        else:
            print("해당 도서가 없음")

    def display_books(self):
        print("\n전체 도서 목록:")
        self.books.display_all()

    def run(self):
        while True:
            print("\n===== 도서 관리 프로그램 =====")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")

            select = input("메뉴 선택: ")

            if select == '1':
                self.add_book()
            elif select == '2':
                self.remove_book()
            elif select == '3':
                self.search_book()
            elif select == '4':
                self.display_books()
            elif select == '5':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 선택입니다. 다시 입력하세요.")


if __name__ == "__main__":
    manager = BookManagement()
    manager.run()
