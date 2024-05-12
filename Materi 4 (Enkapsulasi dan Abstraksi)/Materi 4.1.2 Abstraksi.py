#adalah konsep di mana kita hanya menampilkan informasi penting dari suatu objek dan menyembunyikan informasi yang tidak penting.
from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Segitiga(Bentuk):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

class BelahKetupat(Bentuk):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def luas(self):
        return 0.5 * self.diagonal1 * self.diagonal2

segitiga1 = Segitiga(6, 8)
belah_ketupat1 = BelahKetupat(10, 12)

print(segitiga1.luas())       # output: 24.0
print(belah_ketupat1.luas())  # output: 60.0

