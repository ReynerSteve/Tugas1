from person import Person

# Class Professor juga merupakan turunan dari Person
class Professor(Person):
    def __init__(self, name, phoneNumber, emailAddress, salary: int, staffNumber: int,
                 yearsOfService: int, numberOfClasses: int, address=None):

        # Memanggil konstruktor Person
        super().__init__(name, phoneNumber, emailAddress, address)

        # Attribute internal menggunakan konvensi protected/private
        self._salary = salary
        self._staffNumber = staffNumber
        self._yearsOfService = yearsOfService
        self.numberOfClasses = numberOfClasses

    def supervises(self, student):
        # Relasi supervisi 1..5 dari Professor ke Student
        student.addSupervisor(self)
