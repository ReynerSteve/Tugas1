| Class       | Deskripsi                                                   |
| ----------- | ----------------------------------------------------------- |
| `Person`    | Menyimpan identitas dasar seseorang                         |
| `Student`   | Menyimpan data mahasiswa dan fungsi eligibility pendaftaran |
| `Professor` | Menyimpan data dosen dan relasi supervisi mahasiswa         |
| `Address`   | Menyimpan informasi alamat dan validasi data                |

---

Relasi dalam data tabel

1. Student dan Professor inherit dari Person
2. Person memiliki relasi 0..1 ke Address
3. Professor supervises 0..\* Student

---

Konsep OOP yang digunakan pada kasus ini adalah :

1. Inheritance
2. Encapsulation
3. Association / Multiplicity
4. Method overriding
