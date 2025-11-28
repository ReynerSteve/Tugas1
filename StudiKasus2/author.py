# Representasi data penulis buku
class Author:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    def get_age(self, current_year: int) -> int:
        # Menghitung umur penulis berdasarkan tahun saat ini
        return current_year - self.birth_year
