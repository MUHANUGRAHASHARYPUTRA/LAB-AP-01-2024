def carikoin(koin):
    for jenis in set[koin]:
        if koin.count(jenis) == 1:
            return koin.index(jenis) +1
koin = input("masukkan 8 baris A-Z : ").upper()   
print("koin berbeda ada di baris", carikoin(koin))        
