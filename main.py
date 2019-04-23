import islem
from tkinter import *


print("""        
##############################################                                            # 
#                                            #
#                                            #
#----------- PLAKA TANIMA SİSTEMİ------------#
#                                            #
#                                            #
##############################################""")

print("Resimden plaka tanıma işlemi yapmak için 1'e")
print("Çıkış işlemi yapmak için 2'ye")

try:
    secim = int(input("Seçiminiz:"))

    if secim == 1:
        islem.goruntu()
    elif secim == 2:
        exit()

except ValueError:
    print("Hatalı seçim Lütfen menüden seçim yapınız.")

