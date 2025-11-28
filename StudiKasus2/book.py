from library_item import LibraryItem
from author import Author

# Class Book merupakan turunan dari LibraryItem
class Book(LibraryItem):
    def __init__(self, item_id: int, title: str, isbn: str, author: Author):
        super().__init__(item_id, title)
        self.__isbn = isbn  # Attribute ISBN dibuat private sesuai UML
        self.author = author

    def display_info(self):
        # Override untuk menampilkan info lebih detail
        print(f"Book Title: {self.title}, ISBN: {self.__isbn}, Author: {self.author.name}")

    def calculate_late_fee(self, days_late: int) -> float:
        # Override biaya keterlambatan khusus buku
        return days_late * 2.0
