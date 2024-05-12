class Kucing:
    def __init__(self, jenis, tahun):
        self._jenis = jenis
        self._tahun = tahun
        
    def __info(self):
        print(f"Kucing: {self._jenis} ({self._tahun})")
        
kucing1 = Kucing("Persia", 2018)
kucing1._Kucing__info()  # Output: Kucing: Persia (2018)

print(kucing1._jenis)  # Output: Persia
