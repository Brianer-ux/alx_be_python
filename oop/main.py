from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)          # Uses __str__
    print(repr(my_book))    # Uses __repr__
    del my_book             # Triggers __del__

if __name__ == "__main__":
    main()











































                                                                                [ New File ]
^G Help          ^O Write Out     ^F Where Is      ^K Cut           ^T Execute       ^C Location      M-U Undo         M-A Set Mark     M-] To Bracket   M-B Previous
^X Exit          ^R Read File     ^\ Replace       ^U Paste         ^J Justify       ^/ Go To Line    M-E Redo         M-6 Copy         ^B Where Was     M-F Next
