# Class Address digunakan untuk menyimpan informasi alamat terkait objek Person
class Address:
    def __init__(self, street: str, city: str, state: str, postalCode: int, country: str):
        # Attribute dasar alamat
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country

    def validate(self) -> bool:
        # Mengecek apakah semua field alamat terisi benar
        return all([self.street, self.city, self.state, self.postalCode, self.country])

    def outputAsLabel(self) -> str:
        # Menghasilkan format teks alamat lengkap seperti label/mailing format
        return f"{self.street}, {self.city}, {self.state} {self.postalCode}, {self.country}"
