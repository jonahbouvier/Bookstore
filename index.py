import tkinter as tk
from tkinter import messagebox

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.in_library = False

# Sample book data
book_data = []

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

    
# Main function
if __name__ == "__main__":
    root = tk.Tk()
    app = BookApp(root)
    root.mainloop()
