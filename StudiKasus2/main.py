from author import Author
from book import Book
from library_member import LibraryMember

# Program utama demonstrasi peminjaman buku
if __name__ == "__main__":
    author1 = Author("Tere Liye", 1979)
    print("Author age:", author1.get_age(2025))

    book1 = Book(item_id=1, title="Bumi", isbn="978-602-03-1234-5", author=author1)

    member = LibraryMember(member_id=101, name="Arya")

    member.borrow_item(book1)   # Meminjam buku
    book1.display_info()        # Menampilkan info buku
    print("Late fee (5 days):", book1.calculate_late_fee(5))  # Hitung denda
    member.return_item(book1)   # Mengembalikan buku
