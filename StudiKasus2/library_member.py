from library_item import LibraryItem

# Class LibraryMember representasi anggota perpustakaan
class LibraryMember:
    def __init__(self, member_id: int, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_items: list[LibraryItem] = []  # List item dipinjam

    def borrow_item(self, item: LibraryItem):
        # Menambahkan item ke daftar pinjaman
        self.borrowed_items.append(item)
        print(f"{self.name} borrowed item: {item.title}")

    def return_item(self, item: LibraryItem):
        # Menghapus item dari daftar pinjaman
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            print(f"{self.name} returned item: {item.title}")
        else:
            print("Item not found in borrowed list.")
