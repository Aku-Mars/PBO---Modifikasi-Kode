# adalah konsep dalam pemrograman berorientasi objek yang memungkinkan penggunaan kelas 
# sebagai model atau blue print yang merepresentasikan objek dari dunia nyata atau 
# konsep yang kompleks dalam bentuk yang lebih sederhana.
from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass
    
class Sapi(Hewan):
    def suara(self):
        print("Mooo")
        
class Kambing(Hewan):
    def suara(self):
        print("Mbeee")
        
sapi = Sapi()
sapi.suara()  # output: Mooo

kambing = Kambing()
kambing.suara()  # output: Mbeee
