from person import Person

# Class Student merupakan turunan dari Person (Inheritance)
class Student(Person):
    def __init__(self, name, phoneNumber, emailAddress, studentNumber: int, averageMark: int, address=None):
        # Memanggil konstruktor parent class (Person)
        super().__init__(name, phoneNumber, emailAddress, address)
        self.studentNumber = studentNumber
        self.averageMark = averageMark
        self.supervisors = []  # List untuk menyimpan daftar professor pembimbing

    def isEligibleToEnroll(self, courseName: str) -> bool:
        # Menentukan eligibility berdasarkan nilai rata-rata
        return self.averageMark >= 60

    def getSeminarsTaken(self) -> int:
        # Mengembalikan jumlah professor yang membimbing
        return len(self.supervisors)

    def addSupervisor(self, professor):
        # Menambahkan professor ke daftar pembimbing
        self.supervisors.append(professor)
