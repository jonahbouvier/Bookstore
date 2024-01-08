import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu, Button, Label

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.in_library = False

# Sample book data
book_data = [
    Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy"),
    Book("A Song of Ice and Fire: A Game of Thrones", "George R.R. Martin", "Fantasy"),
    Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
    Book("1984", "George Orwell", "Dystopian"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
    Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"),
    Book("The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien", "Fantasy"),
    Book("Pride and Prejudice", "Jane Austen", "Romance"),
    Book("The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "C.S. Lewis", "Fantasy"),
    Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    Book("Brave New World", "Aldous Huxley", "Dystopian"),
    Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction"),
    Book("The Da Vinci Code", "Dan Brown", "Mystery"),
    Book("The Girl with the Dragon Tattoo", "Stieg Larsson", "Thriller"),
    Book("The Hunger Games", "Suzanne Collins", "Dystopian"),
    # Add more books as needed
]

class BookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Library App")

        # Main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=10, pady=10)

        # Catalog frame on the left
        self.catalog_frame = tk.Frame(self.main_frame)
        self.catalog_frame.pack(side=tk.LEFT, padx=10)

        # Library frame on the right
        self.library_frame = tk.Frame(self.main_frame)
        self.library_frame.pack(side=tk.RIGHT, padx=10)

        # Label for Book Catalog
        catalog_label = tk.Label(self.catalog_frame, text="Book Catalog", font=("Helvetica", 16, "bold"))
        catalog_label.grid(row=0, column=0, sticky="w", pady=5)
        
        # Dropdown menu for Catalog Sorting
        clicked = StringVar()
        clicked.set("Title")
        drop = OptionMenu(root, clicked, "Title", "Genre", "Author")
        drop.pack()

        # Label for My Library
        library_label = tk.Label(self.library_frame, text="My Library", font=("Helvetica", 16, "bold"))
        library_label.grid(row=0, column=0, sticky="w", pady=5)

        # Create book list
        self.create_book_list()

        # Create library list
        self.library_books = []

    def create_book_list(self):
        for book in book_data:
            book_info = f"{book.title} by {book.author} - {book.genre}"
            book_label = tk.Label(self.catalog_frame, text=book_info)
            book_label.grid(sticky="w")

            add_button = tk.Button(self.catalog_frame, text="Add to Library", command=lambda b=book: self.add_to_library(b))
            add_button.grid(row=book_data.index(book) + 1, column=1, padx=(10, 0), sticky="e")

    def add_to_library(self, book):
        if book.in_library:
            messagebox.showinfo("Info", f"{book.title} is already in your library.")
        else:
            book.in_library = True
            self.library_books.append(book)
            messagebox.showinfo("Success", f"{book.title} added to your library.")

        # Refresh library display
        self.display_library()

    def display_library(self):
        # Clear previous library display
        for widget in self.library_frame.winfo_children():
            widget.destroy()

        # Display updated library
        # Label for My Library
        library_label = tk.Label(self.library_frame, text="My Library", font=("Helvetica", 16, "bold"))
        library_label.pack(side=tk.TOP, pady=5)

        for book in self.library_books:
            library_label = tk.Label(self.library_frame, text=f"{book.title} by {book.author} - {book.genre}")
            library_label.pack()

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()
