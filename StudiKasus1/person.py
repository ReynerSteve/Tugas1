from address import Address

# Class Person merupakan superclass yang akan menjadi dasar Student dan Professor
class Person:
    def __init__(self, name: str, phoneNumber: str, emailAddress: str, address: Address = None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.address = address  # Relationship 0..1 dengan Address

    def purchaseParkingPass(self):
        # Contoh proses yang dimiliki oleh semua jenis Person
        print(f"{self.name} has purchased a parking pass.")
