class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.readlines()
        counter = 1
        print('---------------------------------------------------------------------------------')
        for line in lines:
            book = line.strip().split(",")
            print(counter, ')', 'Book Name:', book[0], '- Author:', book[1],
                  '- Release Date:', book[2], '- Number Of Pages:', book[3])
            counter = counter + 1
        print('---------------------------------------------------------------------------------')

    def add(self, name, author, release_date, pages):
        record = name.strip() + ',' + author.strip() + ',' + str(release_date).strip() + ',' + str(pages).strip() + '\n'
        self.file.write(record)
        print('Book added successfully.')
        print('---------------------------------------------------------------------------------')

    def remove(self, name):
        self.file.seek(0)
        lines = self.file.readlines()
        books = [line.strip().split(",") for line in lines]
        found = [name.lower().strip() in books[i][0].lower() for i in range(len(books))]
        if True in found:
            index = found.index(True)
            books.pop(index)
        else:
            print('Book not found.')
            return
        self.file.seek(0)
        self.file.truncate()
        for book in books:
            self.file.write(','.join(book) + '\n')
        print('Book deleted successfully.')
        print('---------------------------------------------------------------------------------')


lib = Library()

while True:
    inpt = input('*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\nQ/q) Quit\nSelect: ')
    if inpt == '1':
        lib.list_books()
    elif inpt == '2':
        print('---------------------------------------------------------------------------------')
        lib.add(input('Book Name: '), input('Author: '), input('Release Date: '), input('Number Of Pages: '))
    elif inpt == '3':
        print('---------------------------------------------------------------------------------')
        lib.remove(str(input('Book Name: ')))
    elif inpt == 'q' or inpt == 'Q':
        del lib
        break
    else:
        print('Invalid Character!')
