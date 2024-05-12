class Kucing:
    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur
        
    def get_nama(self):
        return self._nama
    
    def set_nama(self, nama):
        self._nama = nama
        
    def get_umur(self):
        return self._umur
    
    def set_umur(self, umur):
        self._umur = umur
        
kucing1 = Kucing("Meong", 3)
print(kucing1.get_nama())  # output: Meong
kucing1.set_nama("Kitty")
print(kucing1.get_nama())  # output: Kitty
print(kucing1.get_umur())  # output: 3
kucing1.set_umur(4)
print(kucing1.get_umur())  # output: 4
