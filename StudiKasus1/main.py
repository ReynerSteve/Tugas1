from address import Address
from student import Student
from professor import Professor

# Program utama untuk melakukan demonstrasi objek dan relasi
if __name__ == "__main__":
    # Membuat objek Address
    addr = Address("Jl. Merdeka", "Padang", "Sumbar", 25132, "Indonesia")

    # Membuat objek Professor
    prof = Professor("Dr. Budi", "08991234567", "budi@campus.ac.id",
                     salary=15000000, staffNumber=1122, yearsOfService=10, numberOfClasses=3, address=addr)

    # Membuat objek Student
    student = Student("Arya", "08123456789", "arya@student.ac.id", studentNumber=2023001,
                      averageMark=85, address=addr)

    # Professor membimbing Student
    prof.supervises(student)

    # Output testing
    print(student.name, "supervised by:", len(student.supervisors), "professor(s)")
    print("Eligible to enroll?", student.isEligibleToEnroll("OOP"))
    print("Address label:", addr.outputAsLabel())
