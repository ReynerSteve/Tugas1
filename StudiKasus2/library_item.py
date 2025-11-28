# Kelas dasar item perpustakaan
class LibraryItem:
    def __init__(self, item_id: int, title: str):
        self.item_id = item_id
        self.title = title

    def display_info(self):
        # Menampilkan informasi dasar item
        print(f"ID: {self.item_id} | Title: {self.title}")

    def calculate_late_fee(self, days_late: int) -> float:
        # Biaya keterlambatan default: 1.0 per hari
        return days_late * 1.0
